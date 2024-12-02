from abc import ABCMeta, abstractmethod
from ..brick.Sensor import Sensor
from ..condition.Condition import Condition
from ..Signal import Signal

class Comparison(Condition):
    def __init__(self, sensor: Sensor):
        __metaclass__ = ABCMeta
        self.sensor = sensor
    
    @abstractmethod
    def evaluate(self) -> Signal :
        return