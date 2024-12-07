from models import *
from chaining.StateBuilder import StateBuilder
from exceptions.Exceptions import IncompleBuilderError
from enum import Enum

class BrickType(Enum):
    SENSOR = 0
    DIGITAL_ACTUATOR = 1
    BUZZER = 2

class BrickBuilder:
    def __init__(self, brickName: str, brickType: BrickType, app: 'AppBuilder'):
        self.__name: str = brickName
        self.__app: 'AppBuilder' = app
        self.__type: BrickType = brickType
        self.__pin: int = None
    
    @property
    def type(self) -> BrickType:
        return self.__type

    @property
    def name(self) -> str:
        return self.__name

    def on_pin(self, pinNumber: int) -> 'AppBuilder':
        self.__pin = pinNumber
        return self.__app

    def build(self) -> Brick:
        if self.__pin is None or self.__type not in [
            BrickType.SENSOR,
            BrickType.DIGITAL_ACTUATOR,
            BrickType.BUZZER,
        ]:
            raise IncompleBuilderError(
                "The pin is not defined or the type of brick doesn't exist..."
            )

        match self.__type:
            case BrickType.SENSOR:
                return Sensor(self.__name, self.__pin)
            case BrickType.DIGITAL_ACTUATOR:
                return DigitalActuator(self.__name, self.__pin)
            case BrickType.BUZZER:
                return Buzzer(self.__name, self.__pin)

        return None


class AppBuilder:
    def __init__(self, name: str):
        self.__name: str = name
        self.__bricks: list[BrickBuilder] = []
        self.__states: list['StateBuilder'] = []  # String annotation
        self.__initialState: 'StateBuilder' = None  # String annotation

    def with_sensor(self, sensorName: str) -> BrickBuilder:
        brick = BrickBuilder(sensorName, BrickType.SENSOR, self)
        self.__bricks.append(brick)
        return brick

    def with_digital_actuator(self, actuatorName: str) -> BrickBuilder:
        brick = BrickBuilder(actuatorName, BrickType.DIGITAL_ACTUATOR, self)
        self.__bricks.append(brick)
        return brick

    def with_buzzer(self, buzzerName: str) -> BrickBuilder:
        brick = BrickBuilder(buzzerName, BrickType.BUZZER, self)
        self.__bricks.append(brick)
        return brick

    def with_state(self, stateName: str) -> 'StateBuilder':  # String annotation
        from chaining.StateBuilder import StateBuilder  # Lazy import
        state = StateBuilder(stateName, self.__bricks, self)
        if self.__initialState is None:
            self.__initialState = state
        self.__states.append(state)
        return state

    def with_initial_state(self, stateName: str) -> 'StateBuilder':  # String annotation
        from chaining.StateBuilder import StateBuilder  # Lazy import
        state = StateBuilder(stateName, self.__bricks, self)
        self.__initialState = state
        self.__states.append(state)
        return state

    @property
    def build(self) -> App:
        if self.__initialState is None:
            raise IncompleBuilderError(
                "An initial state is needed in order to instanciate an App"
            )

        brickList: list[Brick] = [brick.build() for brick in self.__bricks]
        stateList: list[State] = [state.build() for state in self.__states]
        
        for state in self.__states :
            for transitionBuilder in state.transitions :
                transitionBuilder.build([brick for brick in brickList if isinstance(brick,Sensor)], stateList)

        initialState: State = self.__initialState.build()

        res = App(self.__name, initialState, stateList, brickList)

        print(res)  # Display the ino
        return res

def create_app(name: str) -> AppBuilder :
    return AppBuilder(name)