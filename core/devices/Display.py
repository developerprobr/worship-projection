from PyQt6.QtGui import QScreen
from PyQt6.QtWidgets import QApplication

from core.devices.Device import Device


class Display(Device):
    def __init__(self, application: QApplication):
        super(Display, self).__init__()

        self.monitors = application.screens()

    def getMonitors(self) -> [QScreen]:
        return self.monitors

    def totalMonitors(self) -> int:
        return len(self.monitors)

    def getAvailableMonitorsForProjection(self) -> [QScreen]:
        monitors = self.monitors

        if self.totalMonitors() > 1:
            monitors.remove(monitors[0])

        return monitors
