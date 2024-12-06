from python.models import *
from python.chaining.StateBuilder import StateBuilder
from python.chaining.ConditionBuilder import ConditionBuilder, SubConditionBuilder

class TransitionBuilder():
    def __init__(self, originStateName : str, nextStateName: str, stateBuilder: StateBuilder):
        self.originStateName : str = originStateName
        self.condition : ConditionBuilder = None
        self.nextStateName = nextStateName
        self.stateBuilder = stateBuilder
        
    def when(self, sensorName: str) -> SubConditionBuilder :
        condition = ConditionBuilder(self)
        subCondition = SubConditionBuilder(sensorName,condition, condition.setCondition)
        self.condition = condition
        return subCondition
    
    
    
    