from models.condition.Condition import Condition
from models.Signal import Signal
from models.condition.Operator import Operator

class LogicalOperator(Condition):
    def __init__(self, left: Condition, right: Condition, operator: Operator):
        super().__init__()
        self.left = left
        self.right = right
        self.operator = operator
        
    def flagNeeded(self) -> bool : 
        return self.left.flagNeeded() or self.right.flagNeeded()
    
    def generateFlagDefinition(self, offset: str) -> str :
        return f"{self.left.generateFlagDefinition(offset+"0") if self.left.flagNeeded() else ''}{'\n' if self.left.flagNeeded() and self.right.flagNeeded() else ''}{self.right.generateFlagDefinition(offset+"1") if self.right.flagNeeded() else ''}"
    
    def generateFlagCheck(self, offset: str) -> str :
        return f"{self.left.generateFlagCheck(offset+"0") if self.left.flagNeeded() else ''}{'\n' if self.left.flagNeeded() and self.right.flagNeeded() else ''}{self.right.generateFlagCheck(offset+"1") if self.right.flagNeeded() else ''}"

    def generateCondition(self, offset: str) -> str:
        return f'{self.left.generateCondition(offset+"0")} {self.operator.value} {self.right.generateCondition(offset+"1")}'
    
    def __str__(self) -> str :
        return f'{str(self.left)} {self.operator.value} {str(self.right)}'