from .Comparison import Comparison
from ..brick.Sensor import Sensor
from ..Signal import Signal

class SimpleComparison(Comparison):
    def __init__(self, sensor: Sensor, value: Signal):
        super().__init__(sensor)
        self.value = value