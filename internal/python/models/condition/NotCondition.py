from models.condition.Condition import Condition
from models.comparison.SimpleComparison import SimpleComparison
from models.Signal import Signal

class NotCondition(Condition):
    def __init__(self, condition: Condition):
        super().__init__()
        self.condition : SimpleComparison = condition
        
    def flagNeeded(self) -> bool : 
        return self.condition.flagNeeded()
    
    def generateFlagDefinition(self, offset: str) -> str :
        return self.condition.generateFlagDefinition(offset)
    
    def generateFlagCheck(self, offset: str) -> str :
        return self.condition.generateFlagCheck(offset)
    
    def generateCondition(self, offset: str) -> str :
        return self.condition.generateCondition(offset)
    
    def __str__(self) -> str :
        return f'!{str(self.condition)}'