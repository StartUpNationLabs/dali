from models.condition.Condition import Condition
from models.Signal import Signal
from models.condition.Operator import Operator

class LogicalOperator(Condition):
    def __init__(self, left: Condition, right: Condition, operator: Operator):
        super().__init__()
        self.left = left
        self.right = right
        self.operator = operator
    
    def evaluate(self):
        if (self.operator is Operator.AND) :
            return (self.left is Signal.HIGH) and (self.right is Signal.HIGH)
        else :
            return (self.left is Signal.HIGH) or (self.right is Signal.HIGH)
    
    def __str__(self) -> str :
        return f'{str(self.left)} {self.operator.value} {str(self.right)}'