from abc import ABCMeta, abstractmethod
from ..Signal import Signal

class Condition():
    def __init__(self) :
        __metaclass__ = ABCMeta
    
    @abstractmethod
    def evaluate(self) -> Signal:
        return