from Condition import Condition
from internal.models.Signal import Signal
from Operator import Operator

class ConstantCondition(Condition):
    def __init__(self, left: Condition, right: Condition, operator: Operator):
        super().__init__()
        self.value = self.computeValue(left, right, operator)
    
    def computeValue(self, left: Condition, right: Condition, operator: Operator) -> Signal:
        if (operator is Operator.AND) :
            return (left is Signal.HIGH) and (right is Signal.HIGH)
        else :
            return (left is Signal.HIGH) or (right is Signal.HIGH)
    
    def evaluate(self):
        return self.value