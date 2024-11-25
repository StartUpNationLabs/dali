from NamedElement import NamedElement
from Transition import Transition
from action.Action import Action

class State(NamedElement):
    def __init__(self, name:str, transitions : list[Transition] = None, actions : list[Action] = None):
        super().__init__(name)
        
        if (transitions == None) :
            self.transitions = []
        else :
            self.transitions = transitions
            
        if (actions == None) :
            self.actions = []
        else :
            self.actions = actions