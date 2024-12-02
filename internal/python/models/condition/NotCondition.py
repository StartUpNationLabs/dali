from models.condition.Condition import Condition
from models.Signal import Signal

class NotCondition(Condition):
    def __init__(self, condition: Condition):
        super().__init__()
        self.condition = condition

    def evaluate(self) :
        return not self.condition.evaluate
    
    def __str__(self) -> str :
        return f'!{str(self.condition)}'