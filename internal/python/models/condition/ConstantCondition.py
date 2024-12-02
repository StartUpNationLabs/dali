from Condition import Condition
from internal.models.Signal import Signal

class ConstantCondition(Condition):
    def __init__(self, value: Signal):
        super().__init__()
        self.value = value
    
    def evaluate(self):
        return self.value