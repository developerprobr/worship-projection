from PyQt6.QtWidgets import QMainWindow, QPushButton
from core import ApplicationSession
from core.projection import ProjectionHandler


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.projectors = []
        self.setWindowTitle('Worship Projection')

        button = QPushButton('Teste')
        self.setCentralWidget(button)

        context = ApplicationSession.context()

        projection_handler = ProjectionHandler()
        projection_handler.startAllProjectors(self)

    def openProjection(self):
        pass
