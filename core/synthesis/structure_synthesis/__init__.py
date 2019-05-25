# -*- coding: utf-8 -*-

"""'structure_synthesis' module contains
number and type synthesis functional interfaces.
"""

from __future__ import annotations

__author__ = "Yuan Chang"
__copyright__ = "Copyright (C) 2016-2019"
__license__ = "AGPL"
__email__ = "pyslvs@gmail.com"

from typing import (
    TYPE_CHECKING,
    Tuple,
    List,
    Sequence,
    Dict,
    Iterable,
    Optional,
)
from time import time
from core.QtModules import (
    Slot,
    qt_image_format,
    Qt,
    QWidget,
    QMenu,
    QAction,
    QIcon,
    QPixmap,
    QListWidgetItem,
    QProgressDialog,
    QSize,
    QCoreApplication,
    QMessageBox,
    QPoint,
    QApplication,
    QImage,
    QPainter,
    QPointF,
    QInputDialog,
    QScrollBar,
)
from core.libs import (
    VJoint,
    Graph,
    link_assortment as l_a,
    contracted_link_assortment as c_l_a,
)
from core.graphics import to_graph, engines
from .thread import LinkSynthesisThread, GraphEnumerateThread
from .Ui_structure_widget import Ui_Form

if TYPE_CHECKING:
    from core.widgets import MainWindowBase

__all__ = ['StructureSynthesis']

Assortment = Sequence[int]


def _link_assortment(links_expr: str) -> Assortment:
    """Return link assortment from expr."""
    return tuple(int(n.split('=')[-1]) for n in links_expr.split(", "))


def compare_assortment(first: Tuple[int, ...], second: Sequence[Tuple[int, ...]]) -> int:
    """Compare assortment."""
    my_len = len(first)
    for i, job in enumerate(second):
        if job == first + (0,) * (len(job) - my_len):
            return i
    return -1


class SynthesisProgressDialog(QProgressDialog):

    """Progress dialog for structure synthesis."""

    def __init__(self, title: str, job_name: str, maximum: int, parent: QWidget):
        super(SynthesisProgressDialog, self).__init__(
            job_name,
            "Interrupt",
            0,
            maximum,
            parent
        )
        self.setWindowTitle(title)
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.resize(400, self.height())
        self.setModal(True)
        self.setValue(0)

    def stop_func(self) -> bool:
        """Return dialog status."""
        try:
            QCoreApplication.processEvents()
            return self.wasCanceled()
        except ValueError:
            return False


class StructureSynthesis(QWidget, Ui_Form):
    """Number and type synthesis widget.

    Calculate the combinations of mechanism family and show the atlas.
    """

    def __init__(self, parent: MainWindowBase):
        """Reference names:

        + IO functions from main window.
        + Table data from PMKS expression.
        + Graph data function from main window.
        """
        super(StructureSynthesis, self).__init__(parent)
        self.setupUi(self)

        # Function references
        self.output_to = parent.output_to
        self.save_reply_box = parent.save_reply_box
        self.input_from = parent.input_from
        self.jointDataFunc = parent.entities_point.data_tuple
        self.linkDataFunc = parent.entities_link.data_tuple
        self.get_graph = parent.get_graph
        self.is_monochrome = parent.monochrome_option.isChecked

        # Splitters
        self.splitter.setStretchFactor(0, 2)
        self.splitter.setStretchFactor(1, 15)

        # Answer list
        self.assortment: Dict[Assortment, List[Assortment]] = {}
        self.answer: List[Graph] = []

        # Signals
        self.NL_input.valueChanged.connect(self.__adjust_structure_data)
        self.NJ_input.valueChanged.connect(self.__adjust_structure_data)
        self.graph_engine.addItems(engines)
        self.structure_list.customContextMenuRequested.connect(
            self.__structure_list_context_menu
        )

        # Context menu
        self.pop_menu_topo = QMenu(self)
        self.add_collection = QAction(
            QIcon(QPixmap(":/icons/collections.png")),
            "Add to collections",
            self
        )
        self.copy_edges = QAction("Copy edges", self)
        self.copy_image = QAction("Copy image", self)
        self.pop_menu_topo.addActions([
            self.add_collection,
            self.copy_edges,
            self.copy_image,
        ])

        self.NL_input_old_value = 0
        self.NJ_input_old_value = 0
        self.clear()

    def clear(self):
        """Clear all sub-widgets."""
        self.edges_text.clear()
        self.l_a_list.clear()
        self.__clear_structure_list()
        self.NL_input.setValue(0)
        self.NJ_input.setValue(0)
        self.NL_input_old_value = 0
        self.NJ_input_old_value = 0
        self.DOF.setValue(1)

    @Slot(name='on_assortment_clear_button_clicked')
    def __clear_assortment(self):
        """Clear the number synthesis list."""
        self.c_l_a_list.clear()
        self.l_a_list.clear()
        self.assortment.clear()

    @Slot(name='on_structure_list_clear_button_clicked')
    def __clear_structure_list(self):
        """Clear the structure list."""
        self.answer.clear()
        self.structure_list.clear()
        self.time_label.setText("")

    @Slot(name='on_from_mechanism_button_clicked')
    def __from_mechanism(self):
        """Reload button: Auto-combine the mechanism from the workbook."""
        joint_data = self.jointDataFunc()
        link_data = self.linkDataFunc()
        if joint_data and link_data:
            graph, _, _, _, _, _ = self.get_graph()
            self.edges_text.setText(str(graph.edges))
        else:
            graph = Graph([])
            self.edges_text.setText("")
        keep_dof_checked = self.keep_dof.isChecked()
        self.keep_dof.setChecked(False)
        self.NL_input.setValue(
            sum(len(vlink.points) > 1 for vlink in link_data) +
            sum(
                len(vpoint.links) - 2 for vpoint in joint_data
                if vpoint.type == VJoint.RP and len(vpoint.links) > 1
            )
        )
        self.NJ_input.setValue(sum(
            (len(vpoint.links) - 1 + int(vpoint.type == VJoint.RP))
            for vpoint in joint_data if len(vpoint.links) > 1
        ))
        self.keep_dof.setChecked(keep_dof_checked)

        # Auto synthesis
        if not graph.edges:
            return
        self.__l_a_synthesis()

    def __adjust_structure_data(self):
        """Update NJ and NL values.

        If user don't want to keep the DOF:
        Change the DOF then exit.
        """
        if not self.keep_dof.isChecked():
            self.DOF.setValue(
                3 * (self.NL_input.value() - 1) -
                2 * self.NJ_input.value()
            )
            return

        # Prepare the input value.
        # + N2: Get the user's adjusted value.
        # + NL_func: Get the another value of parameters (N1) by degrees of freedom formula.
        # + is_above: Is value increase or decrease?
        if self.sender() == self.NJ_input:
            n2 = self.NJ_input.value()

            def nl_func() -> float:
                return ((self.DOF.value() + 2 * n2) / 3) + 1

            is_above = n2 > self.NJ_input_old_value
        else:
            n2 = self.NL_input.value()

            def nl_func() -> float:
                return (3 * (n2 - 1) - self.DOF.value()) / 2

            is_above = n2 > self.NL_input_old_value
        n1 = nl_func()
        while not n1.is_integer():
            n2 += 1 if is_above else -1
            n1 = nl_func()
            if n1 == 0 or n2 == 0:
                break

        # Return the result values.
        # + Value of widgets.
        # + Setting old value record.
        if self.sender() == self.NL_input:
            self.NJ_input.setValue(n1)
            self.NL_input.setValue(n2)
            self.NJ_input_old_value = n1
            self.NL_input_old_value = n2
        else:
            self.NJ_input.setValue(n2)
            self.NL_input.setValue(n1)
            self.NJ_input_old_value = n2
            self.NL_input_old_value = n1

    @Slot(name='on_number_synthesis_button_clicked')
    def __l_a_synthesis(self):
        """Synthesis of link assortment."""
        self.l_a_list.clear()
        self.c_l_a_list.clear()
        self.assortment.clear()

        nl = self.NL_input.value()
        nj = self.NJ_input.value()
        dlg = SynthesisProgressDialog(
            "Link assortment",
            f"Number of links: {nl}\n"
            f"Number of joints: {nj}",
            1,
            self
        )

        @Slot(dict)
        def update_result(assortment: Dict[Assortment, List[Assortment]]):
            """Update results."""
            self.assortment.update(assortment)
            for la, cla in assortment.items():
                self.l_a_list.addItem(QListWidgetItem(", ".join(
                    f"NL{i + 2} = {la[i]}" for i in range(len(la))
                )))
            self.l_a_list.setCurrentRow(0)
            dlg.deleteLater()

        work = LinkSynthesisThread(nl, nj, dlg)
        work.progress_update.connect(dlg.setValue)
        work.size_update.connect(dlg.setMaximum)
        work.result.connect(update_result)
        dlg.show()
        work.start()

    @Slot(int, name='on_l_a_list_currentRowChanged')
    def __c_l_a_synthesis(self, l_a_row: int = 0):
        """Synthesis of contracted link assortment."""
        self.c_l_a_list.clear()
        item = self.l_a_list.item(l_a_row)
        if item is None:
            return

        for c_j in self.assortment[_link_assortment(item.text())]:
            self.c_l_a_list.addItem(QListWidgetItem(", ".join(
                f"NC{i + 1} = {c_j[i]}" for i in range(len(c_j))
            )))
        self.c_l_a_list.setCurrentRow(0)

    def __set_time_count(self, t: float, count: int):
        """Set time and count digit to label."""
        self.time_label.setText(f"{t:.04f} s ({count})")

    def __set_paint_time(self, t: float):
        """Set painting time of atlas."""
        self.paint_time_label.setText(f"{t:.04f}s")

    @Slot(name='on_structure_synthesis_button_clicked')
    def __structure_synthesis(self):
        """Structural synthesis - find by contracted links."""
        self.__clear_structure_list()
        item1 = self.l_a_list.currentItem()
        if item1 is None:
            self.__l_a_synthesis()
            item1 = self.l_a_list.currentItem()
        item2 = self.c_l_a_list.currentItem()
        if item2 is None:
            self.__c_l_a_synthesis()
            item2 = self.c_l_a_list.currentItem()

        try:
            job_l_a = _link_assortment(item1.text())
            job_c_l_a = _link_assortment(item2.text())
        except ValueError:
            return

        self.__structural_combine(((job_l_a, job_c_l_a),), 1)

    @Slot(name='on_structure_synthesis_links_button_clicked')
    def __structure_synthesis_links(self):
        """Structural synthesis - find by links."""
        self.__clear_structure_list()
        item = self.l_a_list.currentItem()
        if item is None:
            self.__l_a_synthesis()
            item = self.l_a_list.currentItem()

        _l_a = _link_assortment(item.text())

        def iterator():
            for _c_l_a in self.assortment[_l_a]:
                yield (_l_a, _c_l_a)

        self.__structural_combine(iterator(), len(self.assortment[_l_a]))

    @Slot(name='on_structure_synthesis_all_button_clicked')
    def __structure_synthesis_all(self):
        """Structural synthesis - find all."""
        self.__clear_structure_list()

        def iterator():
            for k, v in self.assortment.items():
                for s in v:
                    yield (k, s)

        self.__structural_combine(iterator(), sum(len(l) for l in self.assortment.values()))

    def __structural_combine(
        self,
        jobs: Iterable[Tuple[Assortment, Assortment]],
        count: int
    ):
        """Structural combine by iterator."""
        t0 = time()
        dlg = SynthesisProgressDialog(
            "Structural Synthesis",
            f"Number of cases: {count}",
            count,
            self
        )

        @Slot(list)
        def update_result(answer: List[Graph]):
            self.answer = answer
            dlg.deleteLater()
            self.__set_time_count(time() - t0, len(self.answer))
            self.__reload_atlas()

        work = GraphEnumerateThread(jobs, self.graph_degenerate.currentIndex(), dlg)
        work.progress_update.connect(dlg.setValue)
        work.result.connect(update_result)
        dlg.show()
        work.start()

    @Slot(name='on_graph_link_as_node_clicked')
    @Slot(name='on_graph_show_label_clicked')
    @Slot(name='on_reload_atlas_clicked')
    @Slot(int, name='on_graph_engine_currentIndexChanged')
    def __reload_atlas(self, *_):
        """Reload the atlas."""
        scroll_bar: QScrollBar = self.structure_list.verticalScrollBar()
        scroll_pos = scroll_bar.sliderPosition()
        index = self.structure_list.currentRow()
        self.structure_list.clear()

        if not self.answer:
            return

        dlg = SynthesisProgressDialog(
            "Structural Synthesis",
            f"Drawing atlas ({len(self.answer)}) ...",
            len(self.answer),
            self
        )
        dlg.show()
        t0 = time()
        for i, G in enumerate(self.answer):
            QCoreApplication.processEvents()
            if dlg.wasCanceled():
                return
            if self.__draw_atlas(i, G):
                dlg.setValue(i + 1)
            else:
                break
        self.__set_paint_time(time() - t0)
        dlg.setValue(dlg.maximum())
        dlg.deleteLater()
        scroll_bar.setSliderPosition(scroll_pos)
        self.structure_list.setCurrentRow(index)

    def __draw_atlas(self, i: int, g: Graph) -> bool:
        """Draw atlas and return True if done."""
        item = QListWidgetItem(f"No. {i + 1}")
        item.setIcon(to_graph(
            g,
            self.structure_list.iconSize().width(),
            self.graph_engine.currentText(),
            self.graph_link_as_node.isChecked(),
            self.graph_show_label.isChecked(),
            self.is_monochrome()
        ))
        item.setToolTip(
            f"Edge Set: {list(g.edges)}\n"
            f"Link assortment: {l_a(g)}\n"
            f"Contracted Link assortment: {c_l_a(g)}"
        )
        self.structure_list.addItem(item)
        return True

    def __atlas_image(self, row: Optional[int] = None) -> QImage:
        """Capture a result item icon to image."""
        if row is None:
            item: QListWidgetItem = self.structure_list.currentItem()
        else:
            item: QListWidgetItem = self.structure_list.item(row)
        return item.icon().pixmap(self.structure_list.iconSize()).toImage()

    @Slot(QPoint)
    def __structure_list_context_menu(self, point):
        """Context menu for the type synthesis results."""
        index = self.structure_list.currentIndex().row()
        self.add_collection.setEnabled(index > -1)
        self.copy_edges.setEnabled(index > -1)
        self.copy_image.setEnabled(index > -1)
        action = self.pop_menu_topo.exec(self.structure_list.mapToGlobal(point))
        if not action:
            return
        clipboard = QApplication.clipboard()
        if action == self.add_collection:
            self.addCollection(self.answer[index].edges)
        elif action == self.copy_edges:
            clipboard.setText(str(self.answer[index].edges))
        elif action == self.copy_image:
            # Turn the transparent background to white.
            image1 = self.__atlas_image()
            image2 = QImage(image1.size(), image1.format())
            image2.fill(Qt.white)
            painter = QPainter(image2)
            painter.drawImage(QPointF(0, 0), image1)
            painter.end()
            clipboard.setPixmap(QPixmap.fromImage(image2))

    @Slot(name='on_expr_copy_clicked')
    def __copy_expr(self):
        """Copy expression button."""
        string = self.edges_text.text()
        if string:
            QApplication.clipboard().setText(string)
            self.edges_text.selectAll()

    @Slot(name='on_expr_add_collection_clicked')
    def __add_collection(self):
        """Add this expression to collections widget."""
        string = self.edges_text.text()
        if string:
            self.addCollection(eval(string))

    @Slot(name='on_save_atlas_clicked')
    def __save_atlas(self):
        """Saving all the atlas to image file.

        We should turn transparent background to white first.
        Then using QImage class to merge into one image.
        """
        count = self.structure_list.count()
        if not count:
            return

        lateral = self.__save_atlas_ask()
        if not lateral:
            return

        file_name = self.output_to("Atlas image", qt_image_format)
        if not file_name:
            return

        width = self.structure_list.iconSize().width()
        image_main = QImage(QSize(
            lateral * width if count > lateral else count * width,
            ((count // lateral) + bool(count % lateral)) * width
        ), self.__atlas_image(0).format())
        image_main.fill(Qt.transparent)
        painter = QPainter(image_main)
        for row in range(count):
            image = self.__atlas_image(row)
            painter.drawImage(QPointF(
                row % lateral * width,
                row // lateral * width
            ), image)
        painter.end()
        pixmap = QPixmap.fromImage(image_main)
        pixmap.save(file_name)
        self.save_reply_box("Atlas", file_name)

    def __save_atlas_ask(self) -> int:
        """Ask when saving the atlas."""
        lateral, ok = QInputDialog.getInt(
            self,
            "Atlas",
            "The number of lateral:",
            5,
            1
        )
        if not ok:
            return 0
        return lateral

    @Slot(name='on_save_edges_clicked')
    def __save_edges(self):
        """Saving all the atlas to text file."""
        file_name = ""
        count = self.structure_list.count()
        if not count:
            return
        if not file_name:
            file_name = self.output_to(
                "Atlas edges expression",
                ["Text file (*.txt)"]
            )
        if not file_name:
            return
        with open(file_name, 'w', encoding='utf-8') as f:
            f.write('\n'.join(str(G.edges) for G in self.answer))
        self.save_reply_box("edges expression", file_name)

    @Slot(name='on_edges2atlas_button_clicked')
    def __edges2atlas(self):
        """Turn the text files into a atlas image.

        This operation will load all edges to list widget first.
        """
        file_names = self.input_from(
            "Edges data",
            ["Text file (*.txt)"],
            multiple=True
        )
        if not file_names:
            return

        read_data = []
        for file_name in file_names:
            with open(file_name, 'r', encoding='utf-8') as f:
                for line in f:
                    read_data.append(line)

        answer = []
        for edges in read_data:
            try:
                g = Graph(eval(edges))
            except (SyntaxError, TypeError):
                QMessageBox.warning(
                    self,
                    "Wrong format",
                    "Please check text format."
                )
            else:
                answer.append(g)

        if not answer:
            QMessageBox.information(
                self,
                "No data",
                "The graph data is empty."
            )
            return

        self.answer = answer
        self.__set_time_count(0, len(answer))
        self.__reload_atlas()
        self.__save_atlas()
