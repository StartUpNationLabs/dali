from abc import ABCMeta

class Condition():
    def __init__(self) :
        __metaclass__ = ABCMeta
    
    def flagNeeded(self) -> bool : 
        return False
    
    def generateCondition(self, offset: str) -> str:
        return str(self)
    
    def generateFlagDefinition(self, offset: str) -> str :
        return ""
    
    def generateFlagCheck(self, offset: str) -> str :
        return ""