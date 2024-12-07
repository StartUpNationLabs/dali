from models.condition.Condition import Condition
from models.Signal import Signal
from models.condition.Operator import Operator

class LogicalOperator(Condition):
    def __init__(self, left: Condition, right: Condition, operator: Operator):
        super().__init__()
        self.left = left
        self.right = right
        self.operator = operator
    
    def __str__(self) -> str :
        return f'{str(self.left)} {self.operator.value} {str(self.right)}'