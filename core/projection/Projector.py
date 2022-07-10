from PyQt6.QtWidgets import QWidget, QLabel, QHBoxLayout
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QScreen


class Projector(QWidget):
    def __init__(self, display: QScreen):
        super().__init__()

        self._display = display

        self.move(display.geometry().left(), display.geometry().top())
        self.setWindowFlags(Qt.WindowType.WindowStaysOnTopHint | Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)

        layout = QHBoxLayout()
        label = QLabel('Teste 01')
        layout.addWidget(label)
        self.setLayout(layout)

    def start(self) -> None:
        self.showFullScreen()
