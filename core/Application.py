from abc import ABC
from core import ApplicationSession


class Application(ABC):
    def __init__(self):
        super(Application, self).__init__()
        self.context = ApplicationSession.context()
