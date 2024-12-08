from models.NamedElement import NamedElement
from models.Transition import Transition

class State(NamedElement):
    def __init__(self, name:str, transitions = None, actions = None):
        super().__init__(name)
        
        if (transitions == None) :
            self.transitions : list['Transition'] = []
        else :
            self.transitions : list['Transition'] = transitions
            
        if (actions == None) :
            self.actions = []
        else :
            self.actions = actions
    
    def generateCall(self) :
        return f'{self.name}();'
    
    def addTransition(self, transition: Transition) :
        self.transitions.append(transition)

    def __str__(self) -> str :
        return f"""
void {self.name}(){{
{''.join([str(action) + "\n" for action in self.actions]).rstrip()}
{''.join([transition.generateFlag(str(index)) + "\n" for index, transition in enumerate(self.transitions)]).rstrip()}
\tdelay(200);
\twhile(true){{{''.join([transition.generateFlagCheck(str(index)) + "\n" for index, transition in enumerate(self.transitions)]).rstrip()}
    {'\t'.join([transition.generateCondition(str(index)) + "\n" for index, transition in enumerate(self.transitions)]).rstrip()}
\t}}
}}
"""