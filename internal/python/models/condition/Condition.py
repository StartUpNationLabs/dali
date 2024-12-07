from abc import ABCMeta, abstractmethod
from models.Signal import Signal

class Condition():
    def __init__(self) :
        __metaclass__ = ABCMeta