from models.condition.Condition import Condition
from models.Signal import Signal

class ConstantCondition(Condition):
    def __init__(self, value: Signal):
        super().__init__()
        self.value = value
    
    def evaluate(self):
        return self.value
    
    def __str__(self) :
        return 'true' if (self.value is Signal.HIGH) else 'false'