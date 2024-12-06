class IncompleBuilderError(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message

class MissingOperationElement(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message

class InvalidOperation(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message