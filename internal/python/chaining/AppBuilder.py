from internal.python.models import *
from chaining.BrickBuilder import *
from chaining.StateBuilder import StateBuilder
from typing import Self

class AppBuilder():
    def __init__(self, name: str):
        self.name : str = name
        self.bricks : list[BrickBuilder] = []
        self.states : list[StateBuilder] = []
        self.initialState : StateBuilder = None
    
    def sensor(self,sensorName: str) -> BrickBuilder :
        brick = BrickBuilder(sensorName,BrickType.SENSOR, self)
        self.bricks.append(brick)
        return brick
    
    def digitalActuator(self, actuatorName: str) -> BrickBuilder :
        brick = BrickBuilder(actuatorName, BrickType.DIGITAL_ACTUATOR, self)
        self.bricks.append(brick)
        return brick
    
    def buzzer(self, buzzerName: str) -> BrickBuilder :
        brick = BrickBuilder(buzzerName, BrickType.BUZZER, self)
        self.bricks.append(brick)
        return brick
    
    def state(self, stateName: str) -> StateBuilder :
        state = StateBuilder(stateName, self)
        if self.initialState == None :
            self.initialState = state
        self.states.append(state)
        return state
    
    def initialState(self, stateName: str) -> StateBuilder :
        state = StateBuilder(stateName)
        self.initialState = state
        self.states.append(state)
        return state
    
    def build(self) -> App :
        if self.initialState == None :
            raise IncompleBuilderError("An initial state is needed in order to instanciate an App")
        
        brickList : list[Brick] = [brick.build() for brick in self.bricks]
        stateList : list[State] = [state.build() for state in self.states]
        
        initialState : State = self.initialState.build()
        
        res = App(self.name, initialState, stateList, brickList)
        
        print(res) # Display the ino 
        return res