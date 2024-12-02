from Condition import Condition
from ..Signal import Signal

class ConstantCondition(Condition):
    def __init__(self, value: Signal):
        super().__init__()
        self.value = value