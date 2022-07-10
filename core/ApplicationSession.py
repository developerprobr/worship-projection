from core import ApplicationContext

context = ApplicationContext()


class ApplicationSession:
    @staticmethod
    def context() -> ApplicationContext:
        return context

