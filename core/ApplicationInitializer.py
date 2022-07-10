from core import ApplicationSession
from screens import MainWindow


def _startWindow():
    window = MainWindow()
    window.setWindowTitle('Worship Projection')

    return window


class ApplicationInitializer:
    @staticmethod
    def start():
        context = ApplicationSession.context()
        window = _startWindow()
        window.show()
        context.getApp().exec()
