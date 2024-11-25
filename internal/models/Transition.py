from NamedElement import NamedElement
from State import State

class Transition(NamedElement):
    def __init__(self, name:str, nextState: State):
        super().__init__(name)
        self.nextState = nextState