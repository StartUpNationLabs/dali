from python.chaining.Exceptions import MissingOperationElement
from python.chaining.TransitionBuilder import TransitionBuilder
from python.chaining.BrickBuilder import BrickType, BrickBuilder
from python.chaining.StateBuilder import StateBuilder
from python.models import *
from python.dto import *
from typing import Self

class ConditionBuilder() :
    def __init__(self, transitionBuilder: TransitionBuilder, bricks : list[BrickBuilder]):
        self.condition: BaseComparisonDto = None
        self.transitionBuilder = transitionBuilder
        self.bricks = bricks
    
    def setCondition(self, condition: BaseComparisonDto):
        self.condition = condition
        
    def logicalCondition(self, operator: Operator, sensorName: str) -> 'SubConditionBuilder' :
        if (self.condition == None) :
            raise InvalidOperation("Try to use a logical operator when they're is not left condition to use on.")
        if (sensorName == None) :
            raise MissingOperationElement("Try to read value of undefined sensor, please set a value")
        if (sensorName not in [brick.name for brick in self.bricks if brick.type == BrickType.SENSOR]):
            raise InvalidOperation("The given sensor name don't reference any given sensor of the app.")

        tmpCondition : LogicalComparisonDto = LogicalComparisonDto(operator, self.condition, None)
        self.condition = tmpCondition
        return SubConditionBuilder(sensorName,self, tmpCondition.setCondition)
        
        
    def andCondition(self, sensorName: str) -> 'SubConditionBuilder':
        self.logicalCondition(Operator.AND, sensorName)
    
    def orCondition(self, sensorName: str) -> 'SubConditionBuilder':
        self.logicalCondition(Operator.OR, sensorName)
    
    def endTransition(self) -> StateBuilder :
        return self.transitionBuilder.stateBuilder
        
class SubConditionBuilder:
    def __init__(self, sensorName: str, conditionBuilder: ConditionBuilder, setCondition: function):
        self.sensorName = sensorName
        self.builder = conditionBuilder
        self.setCondition = setCondition
    
    def asValue(self, value: Signal) -> ConditionBuilder:
        if (self.sensorName == None) :
            raise MissingOperationElement("Try to read value of undefined sensor, please set a value")
        
        if (value == None) :
            raise MissingOperationElement("Try to read a sensor data, but with an undefined value to ensure the comparison")
        
        self.setCondition(SimpleComparisonDto(self.sensorName,value))
        return self.builder
    
    def fromValueToValue(self, fromValue: Signal, toValue: Signal) -> ConditionBuilder:
        if (self.sensorName == None) :
            raise MissingOperationElement("Try to read value of undefined sensor, please set a value")
        
        if (fromValue == None) :
            raise MissingOperationElement("Try to read a sensor data, but with an undefined starting value to ensure the comparison")
        
        if (toValue == None) :
            raise MissingOperationElement("Try to read a sensor data, but with an undefined destination value to ensure the comparison")
        
        self.setCondition(EdgeComparisonDto(self.sensorName,fromValue, toValue))
        return self.builder
        
    def asValueHigh(self) -> ConditionBuilder:
        return self.asValue(Signal.HIGH)
    
    def asValueLow(self) -> ConditionBuilder:
        return self.asValue(Signal.LOW)
    
    def fromLowToHigh(self) -> ConditionBuilder :
        return self.fromValueToValue(Signal.LOW, Signal.HIGH)
     
    def fromHighToLow(self) -> ConditionBuilder :
        return self.fromValueToValue(Signal.HIGH, Signal.LOW)
    
        