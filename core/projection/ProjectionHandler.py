from core.factory import ProjectionFactory
from core.projection import Projector
from core import Application


class ProjectionHandler(Application.Application):  # TODO: It's necessary to fix it soon
    def __init__(self, parent):
        super(ProjectionHandler, self).__init__()

        self._parent = parent
        self._parent.projectors = []
        self.context.setProjectors(self._parent.projectors)
        self._projectors = self._parent.projectors

    def createAllProjectors(self) -> [Projector]:
        monitors = self.context.getDisplay().getAvailableMonitorsForProjection()

        for monitor in monitors:
            self._projectors.append(ProjectionFactory.createProjection(monitor))

        return self._projectors

    def startAllProjectors(self):
        for projector in self._projectors:
            projector.start()
