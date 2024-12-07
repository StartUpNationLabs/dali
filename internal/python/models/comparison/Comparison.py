from abc import ABCMeta, abstractmethod
from models.brick.Sensor import Sensor
from models.condition.Condition import Condition
from models.Signal import Signal

class Comparison(Condition):
    def __init__(self, sensor: Sensor):
        __metaclass__ = ABCMeta
        self.sensor = sensor