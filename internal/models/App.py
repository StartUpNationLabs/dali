from NamedElement import NamedElement
from State import State
from brick.Brick import Brick

class App(NamedElement):
    def __init__(self, name: str, initialState: State, states: list[State], bricks :list[Brick] = None):
        super().__init__(name)
        
        self.initialState = initialState
        self.states = states
        
        if (bricks == None) :
            self.bricks = []
        else :
            self.bricks = bricks