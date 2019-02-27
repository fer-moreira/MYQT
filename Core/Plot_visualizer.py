from PyQt5.QtWidgets import QApplication, QMainWindow

from assets.UI.Scripts.PlotVisualizer import Ui_PlotView

class PlotVisualizer(QMainWindow, Ui_PlotView):
    def __init__(self, parent=None):
        super(PlotVisualizer, self).__init__(parent)
        self.setupUi(self)
        self.show()