from models import *

if __name__ == '__main__' :
    button = Sensor("button", 0)
    led = DigitalActuator("led",1)
    buzzer = Buzzer("buzzer",2)
    
    ledOn = DigitalAction(led, Signal.HIGH)
    buzzerPlay = MelodyAction(buzzer,120,5)
    
    buttonHigh = SimpleComparison(button, Signal.HIGH)
    
    conditionFalse = ConstantCondition(Signal.LOW)
    conditionNot = NotCondition(conditionFalse)
    conditionAnd = LogicalOperator(buttonHigh, conditionNot, Operator.AND)
    
    state2 = State("state2", transitions=[], actions=[buzzerPlay])
    
    transition = Transition(state2, conditionFalse)
    transition2 = Transition(state2, conditionNot)
    transition3 = Transition(state2, conditionAnd)
    
    state = State("state1", transitions=[transition, transition2, transition3], actions=[ledOn])
    
    app = App("Test App", state, states=[state,state2], bricks=[button, led, buzzer])
    
    print(app)