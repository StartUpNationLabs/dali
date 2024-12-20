from abc import ABC, abstractmethod
from models import Signal, DigitalAction, MelodyAction, Action
import chaining.AppBuilder as AppModule
import chaining.StateBuilder as StateModule
from exceptions import InvalidOperation, IncompleBuilderError
from typing import Self

class ActionBuilder(ABC):
    @abstractmethod
    def build(self) -> Action:
        pass

class DigitalActionBuilder(ActionBuilder):
    def __init__(self, actuator: 'AppModule.BrickBuilder', value: Signal):
        self.__actuator = actuator
        self.__value = value
    
    def build(self) -> DigitalAction:
        return DigitalAction(self.__actuator.build(), self.__value)

class MelodyActionBuilder(ActionBuilder):
    def __init__(self, actuator: 'AppModule.BrickBuilder', frequency: int, stateBuilder: 'StateModule.StateBuilder') :
        if (frequency < 0 or frequency > 65535):
            raise InvalidOperation(f"The given frequency of {frequency} for the actuator named {self.__actuator.name} is not between 0 and 65 535.")
        
        self.__actuator = actuator
        self.__frequency = frequency
        self.__duration = None
        self.__stateBuilder = stateBuilder
    
    def during(self, duration : int) -> Self:
        if (duration < 0) :
            raise InvalidOperation(f"The given duration of {duration} ms for the actuator named {self.__actuator.name} is below 0 ms.")
        
        self.__duration = duration
        return self

    @property
    def end_melody(self):
        return self.__stateBuilder
    
    def build(self) -> MelodyAction :
        if (self.__frequency == None) :
            raise IncompleBuilderError("You can't make the buzzer tone without a specific frequency, try calling the .at_frequency method.")
        
        return MelodyAction(self.__actuator.build(),self.__frequency, self.__duration)