class LanguageException(RuntimeError):
    def __init__(self, component, message: str):
        component.trace()
        self.row = component.row
        self.message = message

    def __str__(self):
        return f"{self.row.obtain_traces()}\n{type(self).__name__}: {self.message}"
