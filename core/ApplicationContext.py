import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from core.devices import Display


class ApplicationContext:
    def __init__(self):
        self._application = QApplication(sys.argv)
        self._display: Display = Display(self._application)

    def getDisplay(self) -> Display:
        return self._display

    def getApp(self) -> QApplication:
        return self._application
