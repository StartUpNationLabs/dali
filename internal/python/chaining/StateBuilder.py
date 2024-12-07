from models import *
from exceptions import InvalidOperation
from typing import Self
from chaining.ActionBuilder import MelodyActionBuilder, DigitalActionBuilder, ActionBuilder
from chaining.AppBuilder import *
from chaining.ConditionBuilder import ConditionBuilder, SubConditionBuilder
from dto import ConstantConditionDto

class StateBuilder:
    def __init__(self, stateName: str, bricks: list['BrickBuilder'], app: 'AppBuilder'):
        self.__name = stateName
        self.__actions: list['ActionBuilder'] = []
        self.__transitions : list['TransitionBuilder'] = []
        self.__bricks = bricks
        self.__app = app
    
    @property
    def transitions(self) -> list['TransitionBuilder'] :
        return self.__transitions

    def add_transition_to(self, nextStateName: str) -> 'TransitionBuilder':
        transition = TransitionBuilder(self.__name, nextStateName, self, self.__bricks)
        self.__transitions.append(transition)
        return transition
    
    def __switch_digital_actuator_to_value(self, actuatorName: str, value: Signal) -> Self:
        from chaining.AppBuilder import BrickType
        if (actuatorName == None or actuatorName == ''):
            raise InvalidOperation("Your can't switch on an actuator with an undefined name.")
        
        actuator = next((brick for brick in self.__bricks if (brick.name == actuatorName and brick.type in [BrickType.DIGITAL_ACTUATOR, BrickType.BUZZER])),None)
        
        if (actuator == None) :
            raise InvalidOperation("The actuator name you gave is not an existing digital actuator. Try creating it before calling the switch_on function.")
        
        action = DigitalActionBuilder(actuator, value)
        self.__actions.append(action)
        return self
    
    def switch_on(self, actuatorName: str):
        return self.__switch_digital_actuator_to_value(actuatorName, Signal.HIGH)
    
    def switch_off(self, actuatorName: str):
        return self.__switch_digital_actuator_to_value(actuatorName, Signal.LOW)
    
    def play_music_with_buzzer(self, buzzerName: str, frequency: int) -> 'MelodyActionBuilder':
        from chaining.AppBuilder import BrickType
        if (buzzerName == None or buzzerName == ''):
            raise InvalidOperation("Your can't play music on a buzzer with an undefined name.")
        
        buzzer = next((brick for brick in self.__bricks if (brick.name == buzzerName and brick.type == BrickType.BUZZER)),None)
        
        if (buzzer == None) :
            raise InvalidOperation("The buzzer name you gave is not an existing buzzer. Try creating it before calling the play_music function.")
        
        action = MelodyActionBuilder(buzzer, frequency, self)
        self.__actions.append(action)
        return action

    @property
    def end_state(self) -> 'AppBuilder':
        return self.__app

    def build(self) -> State:
        return State(self.__name, actions= [action.build() for action in self.__actions])


class TransitionBuilder:
    def __init__(self, originStateName: str, nextStateName: str, stateBuilder: StateBuilder, bricks: list['BrickBuilder']):
        self.__originStateName: str = originStateName
        self.__condition: 'ConditionBuilder' = None
        self.__nextStateName = nextStateName
        self.__stateBuilder = stateBuilder
        self.__bricks = bricks

    def when(self, sensorName: str) -> 'SubConditionBuilder':
        condition = ConditionBuilder(self, self.__stateBuilder, self.__bricks)
        subCondition = SubConditionBuilder(sensorName, condition, condition.setCondition)
        self.__condition = condition
        return subCondition
    
    @property
    def when_actions_are_finished(self) -> StateBuilder:
        self.__condition = ConstantConditionDto(Signal.HIGH)
        return self.__stateBuilder
    
    def build(self, bricks: list[Brick], states: list[State]) :
        condition: Condition = self.__condition.build(bricks)
        
        originState = next((state for state in states if state.name == self.__originStateName),None)
        nextState = next((state for state in states if state.name == self.__nextStateName),None)
        
        if originState == None or nextState == None :
            raise InvalidOperation("The origin state or the next state of one transition don't exist.")
        
        transition = Transition(nextState.generateCall,condition)
        originState.addTransition(transition)
        return transition
