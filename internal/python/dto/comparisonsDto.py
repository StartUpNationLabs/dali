from models import *
from exceptions.Exceptions import InvalidOperation
from abc import ABCMeta, abstractmethod

class BaseComparisonDto():
    def __init__(self):
        __metaclass__ = ABCMeta
    
    @abstractmethod
    def build(self, bricks: list[Sensor]) -> Condition:
        pass

class SimpleComparisonDto(BaseComparisonDto):
    def __init__(self, sensorName: str, value: Signal):
        self.sensorName = sensorName
        self.value = value
    
    def build(self, bricks: list[Sensor]) -> SimpleComparison :
        if (self.sensorName == None or self.sensorName == '') :
            raise InvalidOperation("The provided sensor name is empty")
        sensor = next((element for element in bricks if element.name == self.sensorName),None)
        if (sensor == None):
            raise InvalidOperation("The provided sensor name don't exist in the appBuilder.")
        return SimpleComparison(sensor,self.value)

class EdgeComparisonDto(BaseComparisonDto):
    def __init__(self, sensorName: str, fromValue: Signal, toValue: Signal):
        self.sensorName = sensorName
        self.fromValue = fromValue
        self.toValue = toValue
    
    def build(self, bricks: list[Sensor]) -> EdgeComparison :
        if (self.sensorName == None or self.sensorName == '') :
            raise InvalidOperation("The provided sensor name is empty")
        sensor = next((element for element in bricks if element.name == self.sensorName),None)
        if (sensor == None):
            raise InvalidOperation("The provided sensor name don't exist in the appBuilder.")
        return EdgeComparison(sensor,self.fromValue,self.toValue)

class NotComparisonDto(BaseComparisonDto):
    def __init__(self, comparisonDto: BaseComparisonDto):
        self.__condition : SimpleComparisonDto = comparisonDto
    
    def build(self, bricks: list[Sensor]) -> NotCondition :
        return NotCondition(self.__condition.build(bricks))

class LogicalComparisonDto(BaseComparisonDto):
    def __init__(self, operator: Operator, left : BaseComparisonDto, right : BaseComparisonDto):
        self.operator = operator
        self.left = left
        self.right = right
    
    def setCondition(self, condition: BaseComparisonDto):
        self.right = condition
    
    def build(self, bricks: list[Sensor]) -> LogicalOperator:
        left = self.left.build(bricks)
        right = self.right.build(bricks)
        
        return LogicalOperator(left,right,self.operator)
        