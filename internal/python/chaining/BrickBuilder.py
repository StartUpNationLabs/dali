from internal.python.models import *
from Exceptions import IncompleBuilderError
from AppBuilder import AppBuilder
from enum import Enum

class BrickType(Enum):
    SENSOR = 0
    DIGITAL_ACTUATOR = 1
    BUZZER = 2

class BrickBuilder():
    def __init__(self, brickName: str, brickType: BrickType , app : App) :
        self.name = brickName
        self.app = app
        self.type = brickType
        self.pin = None
    
    def on_pin(self, pinNumber: int) -> AppBuilder :
        self.pin = pinNumber
        return self.app
    
    def build(self) -> Brick : 
        if self.pin == None or self.type not in [BrickType.SENSOR, BrickType.DIGITAL_ACTUATOR, BrickType.BUZZER] :
            raise IncompleBuilderError("The pin is not defined or the type of brick don't exist...")
        
        match self.type:
            case BrickType.SENSOR :
                return Sensor(self.name,self.pin)
            case BrickType.DIGITAL_ACTUATOR :
                return DigitalActuator(self.name,self.pin)
            case BrickType.BUZZER :
                return Buzzer(self.name,self.pin)
            
        return None
                
if __name__ == '__main__':
    app = (AppBuilder("test")
           .buzzer("buzzerTest").on_pin(1)
           .sensor("sensorTest").on_pin(2)
           .digitalActuator("digitalActuatorTest").on_pin(3)
           .state("state1")
               .addTransitionTo("state2")
                   .when("sensorTest").fromHighToLow()
                   .andCondition("sensorTest").asValueHigh()
                   .endTransition()
               .endState()
           .build())

            
                        


