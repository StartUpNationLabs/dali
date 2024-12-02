from ..brick.Sensor import Sensor
from ..condition.Condition import Condition

class Comparison(Condition):
    def __init__(self, sensor: Sensor):
        self.sensor = sensor