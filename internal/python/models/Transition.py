from models.State import State
from models.condition.Condition import Condition

class Transition():
    def __init__(self, nextState: State, condition: Condition):
        self.nextState = nextState
        self.condition = condition
    
    def __str__(self) -> str :
        return f"""
\t\tif({str(self.condition)}){{
\t\t\t{self.nextState.generateCall()}
\t\t}}"""