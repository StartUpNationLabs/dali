from exceptions.Exceptions import MissingOperationElement
from chaining.AppBuilder import *
from chaining.StateBuilder import *
import chaining 
from models import *
from dto import *
from typing import Callable

class ConditionBuilder:
    def __init__(self, transitionBuilder: 'chaining.TransitionBuilder', stateBuilder: 'chaining.StateBuilder', bricks: list['BrickBuilder']):
        self.__condition: BaseComparisonDto = None
        self.__transitionBuilder = transitionBuilder
        self.__stateBuilder = stateBuilder
        self.__bricks = bricks

    def setCondition(self, condition: BaseComparisonDto):
        self.__condition = condition

    def logicalCondition(self, operator: Operator, sensorName: str) -> 'SubConditionBuilder':
        from chaining.AppBuilder import BrickType
        
        if self.__condition is None:
            raise InvalidOperation("Try to use a logical operator when there is no left condition to use on.")
        if sensorName is None:
            raise MissingOperationElement("Try to read the value of an undefined sensor, please set a value.")
        if sensorName not in [brick.name for brick in self.__bricks if brick.type == BrickType.SENSOR]:
            raise InvalidOperation("The given sensor name does not reference any given sensor of the app.")

        tmpCondition: LogicalComparisonDto = LogicalComparisonDto(operator, self.__condition, None)
        self.__condition = tmpCondition
        return SubConditionBuilder(sensorName, self, tmpCondition.setCondition)

    def and_condition(self, sensorName: str) -> 'SubConditionBuilder':
        return self.logicalCondition(Operator.AND, sensorName)

    def or_condition(self, sensorName: str) -> 'SubConditionBuilder':
        return self.logicalCondition(Operator.OR, sensorName)

    @property
    def end_transition(self) -> 'StateBuilder':
        return self.__stateBuilder
    
    @property
    def build(self) -> Condition :
        return self.__condition.build(self.__bricks)
        
class SubConditionBuilder:
    def __init__(self, sensorName: str, conditionBuilder: ConditionBuilder, setCondition: Callable):
        self.__sensorName = sensorName
        self.__builder = conditionBuilder
        self.__setCondition = setCondition

    def asValue(self, value: Signal) -> ConditionBuilder:
        if self.__sensorName is None:
            raise MissingOperationElement("Try to read the value of an undefined sensor, please set a value.")

        if value is None:
            raise MissingOperationElement("Try to read sensor data, but with an undefined value to ensure the comparison.")

        self.__setCondition(SimpleComparisonDto(self.__sensorName, value))
        return self.__builder

    def fromValueToValue(self, fromValue: Signal, toValue: Signal) -> ConditionBuilder:
        if self.__sensorName is None:
            raise MissingOperationElement("Try to read the value of an undefined sensor, please set a value.")

        if fromValue is None:
            raise MissingOperationElement("Try to read sensor data, but with an undefined starting value to ensure the comparison.")

        if toValue is None:
            raise MissingOperationElement("Try to read sensor data, but with an undefined destination value to ensure the comparison.")

        self.__setCondition(EdgeComparisonDto(self.__sensorName, fromValue, toValue))
        return self.__builder

    @property
    def have_high_value(self) -> ConditionBuilder:
        return self.asValue(Signal.HIGH)

    @property
    def have_low_value(self) -> ConditionBuilder:
        return self.asValue(Signal.LOW)

    @property
    def go_from_low_to_high(self) -> ConditionBuilder:
        return self.fromValueToValue(Signal.LOW, Signal.HIGH)

    @property
    def go_from_high_to_low(self) -> ConditionBuilder:
        return self.fromValueToValue(Signal.HIGH, Signal.LOW)
    
        