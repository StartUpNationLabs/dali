from python.models import *
from python.chaining.TransitionBuilder import TransitionBuilder
from python.chaining.AppBuilder import AppBuilder

class StateBuilder():
    def __init__(self, stateName: str, app: AppBuilder):
        self.name = stateName
        self.actions = []
        self.transitions = []
        self.app = app
    
    def addTransitionTo(self, nextStateName : str) -> TransitionBuilder :
        transition = TransitionBuilder(self.name, nextStateName)
        self.transitions.append(transition)
        return transition
        
    def endState(self) -> AppBuilder :
        return self.app
    
    def build(self) -> State :
        return State(self.name, self.actions)