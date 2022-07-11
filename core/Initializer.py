from core import ApplicationSession
from core.projection import ProjectionHandler
from screens import MainWindow


def _startWindow():
    window = MainWindow()
    window.setWindowTitle('Worship Projection')

    return window


def _createProjectors(window: MainWindow):
    projection_handler = ProjectionHandler(window)
    projection_handler.createAllProjectors()


class Initializer:
    @staticmethod
    def start():
        context = ApplicationSession.context()
        window = _startWindow()
        window.show()
        context.getApp().exec()

        context.setMainWindow(window)
        context.setProjectors(_createProjectors(window))
