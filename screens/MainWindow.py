from PyQt6.QtWidgets import QMainWindow, QPushButton
from core import ApplicationSession


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Worship Projection')

        button = QPushButton('Teste')
        self.setCentralWidget(button)

        context = ApplicationSession.context()
        context.getDisplay().getAvailableMonitorsForProjection()

    def openProjection(self):
        pass
