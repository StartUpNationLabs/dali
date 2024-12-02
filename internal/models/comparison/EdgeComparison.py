from Comparison import Comparison
from ..brick.Sensor import Sensor
from ..Signal import Signal

class EdgeComparison(Comparison):
    def __init__(self, sensor: Sensor, fromValue: Signal, toValue: Signal):
        super().__init__(sensor)
        self.fromValue = fromValue
        self.toValue = toValue