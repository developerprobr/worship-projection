from core.factory import ProjectionFactory
from core.projection import Projector
from core import Application


class ProjectionHandler(Application.Application):  # TODO: It's necessary to fix it soon
    def __init__(self):
        super(ProjectionHandler, self).__init__()

        self._projectors: [Projector] = []

    def startAllProjectors(self, parent):
        monitors = self.context.getDisplay().getAvailableMonitorsForProjection()

        for monitor in monitors:
            parent.projectors.append(ProjectionFactory.createProjection(monitor))
            self._projectors = parent.projectors

            for projector in self._projectors:
                projector.start()
