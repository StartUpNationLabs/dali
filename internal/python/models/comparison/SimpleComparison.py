from models.comparison.Comparison import Comparison
from models.brick.Sensor import Sensor
from models.Signal import Signal

class SimpleComparison(Comparison):
    def __init__(self, sensor: Sensor, value: Signal):
        super().__init__(sensor)
        self.value = value
    
    def __str__(self) -> str :
        return f'(digitalRead({self.sensor.pin}) == {self.value.value})'