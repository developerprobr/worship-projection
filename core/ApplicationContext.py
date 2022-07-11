import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from core.devices import Display


class ApplicationContext:
    def __init__(self):
        self._application = QApplication(sys.argv)
        self._display: Display = Display(self._application)
        self._main_window: QMainWindow | None = None
        self._projectors = []

    def setMainWindow(self, window: QMainWindow) -> None:
        self._main_window = window

    def setProjectors(self, projectors) -> None:
        self._projectors = projectors

    def getDisplay(self) -> Display:
        return self._display

    def getApp(self) -> QApplication:
        return self._application

    def getWindow(self) -> QMainWindow:
        return self._main_window

    def getProjectors(self):
        return self._projectors
