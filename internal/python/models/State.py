from models.NamedElement import NamedElement

class State(NamedElement):
    def __init__(self, name:str, transitions = None, actions = None):
        super().__init__(name)
        
        if (transitions == None) :
            self.transitions = []
        else :
            self.transitions = transitions
            
        if (actions == None) :
            self.actions = []
        else :
            self.actions = actions
    
    def generateCall(self) :
        return f'{self.name}();'

    def __str__(self) -> str :
        return f"""
void {self.name}(){{
{''.join([str(action) + "\n" for action in self.actions]).rstrip()}
    
    while(true){{
        {'\t'.join([str(transition) + "\n\t" for transition in self.transitions]).rstrip()}
    }}
}}
"""