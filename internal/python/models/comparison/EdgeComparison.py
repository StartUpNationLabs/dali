from models.comparison.Comparison import Comparison
from models.brick.Sensor import Sensor
from models.Signal import Signal

class EdgeComparison(Comparison):
    def __init__(self, sensor: Sensor, fromValue: Signal, toValue: Signal):
        super().__init__(sensor)
        self.fromValue = fromValue
        self.toValue = toValue