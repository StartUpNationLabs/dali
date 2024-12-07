from models.condition.Condition import Condition
from typing import Callable

class Transition():
    def __init__(self, nextStateCall: Callable, condition: Condition):
        self.nextStateCall = nextStateCall
        self.condition = condition
    
    def generateFlag(self, offset: str) -> str:
        return self.condition.generateFlagDefinition(offset)
    
    def generateFlagCheck(self, offset: str) -> str :
        return self.condition.generateFlagCheck(offset)
    
    def generateCondition(self, offset: str) -> str :
        return f"""
\t\tif({str(self.condition.generateCondition(offset))}){{
\t\t\t{self.nextStateCall()}
\t\t}}
"""
    
    def __str__(self) -> str :
        return f"""
\t\tif({str(self.condition)}){{
\t\t\t{self.nextStateCall()}
\t\t}}"""