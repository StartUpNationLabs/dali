from models import App, State, Signal, DigitalActuator, Buzzer, Sensor, DigitalAction, MelodyAction, ConstantCondition, NotCondition, LogicalOperator, Operator, Transition

if __name__ == '__main__' :
    button = Sensor("button", 0)
    led = DigitalActuator("led",1)
    buzzer = Buzzer("buzzer",2)
    
    ledOn = DigitalAction(led, Signal.HIGH)
    buzzerPlay = MelodyAction(buzzer,120,5)
    
    conditionTrue = ConstantCondition(Signal.HIGH)
    conditionNot = NotCondition(conditionTrue)
    conditionAnd = LogicalOperator(conditionTrue, conditionNot, Operator.Operator.AND)
    
    state2 = State("state2", transitions=[], actions=[buzzerPlay])
    
    transition = Transition(state2, conditionTrue)
    transition2 = Transition(state2, conditionNot)
    transition3 = Transition(state2, conditionAnd)
    
    state = State("state1", transitions=[transition, transition2, transition3], actions=[ledOn])
    
    app = App("Test App", state, states=[state,state2], bricks=[button, led, buzzer])
    
    print(app)