from PyQt6.QtWidgets import QWidget, QHBoxLayout
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QScreen


class ProjectionWindow(QWidget):
    def __init__(self, display: QScreen):
        super().__init__()

        self.move(display.geometry().left(), display.geometry().top())
        self.setWindowFlags(Qt.WindowType.WindowStaysOnTopHint | Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)

    def start(self) -> None:
        self.showFullScreen()
