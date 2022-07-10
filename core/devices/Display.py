from PyQt6.QtGui import QScreen
from PyQt6.QtWidgets import QApplication

from core.devices.Device import Device


class Display(Device):
    def __init__(self, application: QApplication):
        super(Display, self).__init__()

        self.monitors = application.screens()
        self._available_monitors = self._availableMonitors()

    def getMonitors(self) -> [QScreen]:
        return self.monitors

    def totalMonitors(self) -> int:
        return len(self.monitors)

    def _availableMonitors(self) -> [QScreen]:
        monitors = self.monitors

        if self.totalMonitors() > 1:
            monitors.remove(self.monitors[0])

        print('Total :', self.totalMonitors())
        for monitor in monitors:
            print('size: ', monitor.size())

        return monitors

    def getAvailableMonitorsForProjection(self) -> [QScreen]:
        return self._available_monitors
