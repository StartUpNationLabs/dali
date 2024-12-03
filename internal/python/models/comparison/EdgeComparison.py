from models.comparison.Comparison import Comparison
from models.brick.Sensor import Sensor
from models.Signal import Signal
from models.condition.Operator import Operator

class EdgeComparison(Comparison):
    def __init__(self, sensor: Sensor, fromValue: Signal, toValue: Signal):
        super().__init__(sensor)
        self.fromValue = fromValue
        self.toValue = toValue
    
    def __str__(self) -> str :
        return f'(last{self.sensor.name} == {self.fromValue.value} {Operator.AND.value} (last{self.sensor.name} = digitalRead({self.sensor.name})) == {self.toValue.value})'