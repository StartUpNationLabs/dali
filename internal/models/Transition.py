from NamedElement import NamedElement
from State import State
from condition.Condition import Condition

class Transition(NamedElement):
    def __init__(self, name:str, nextState: State, condition: Condition):
        super().__init__(name)
        self.nextState = nextState
        self.condition = condition