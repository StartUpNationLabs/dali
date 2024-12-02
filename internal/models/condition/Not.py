from Condition import Condition
from ..Signal import Signal

class NotCondition(Condition):
    def __init__(self, value: Signal):
        super().__init__()
        
        if value is Signal.HIGH:
            self.value = Signal.LOW
        else :
            self.value = Signal.HIGH