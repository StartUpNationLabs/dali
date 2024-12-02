from models.brick.Sensor import Sensor
from models.action.DigitalAction import DigitalAction
from models.State import State
from models.App import App
from models.brick.Digital import Digital
from models.Signal import Signal

if __name__ == '__main__' :
    
    actuator = Digital("buzzer",2)
    action = DigitalAction(actuator,Signal.HIGH)
    state = State("state1")
    button = Sensor("button",1)
    app = App("test",state, [state], [button])
    
    print(app)