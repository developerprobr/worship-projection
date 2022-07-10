from core import ApplicationSession, ApplicationContext
from core.devices import Display
from core.exception import FactoryException
from screens import ProjectionWindow
from PyQt6.QtGui import QScreen


class ProjectionFactory:
    @staticmethod
    def createProjection(display: QScreen) -> ProjectionWindow:

        if display is None:
            raise FactoryException('It\'s necessary to specify the display.')

        context: ApplicationContext = ApplicationSession.context()
        display_devices: Display = context.getDisplay()
        display_list: [QScreen] = display_devices.getAvailableMonitorsForProjection()

        selected_display = display in display_list

        if selected_display is not None:
            window = ProjectionWindow(display)

            return window

        raise FactoryException('It was not possible to find the specified display.')
