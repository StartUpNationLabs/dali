from models.NamedElement import NamedElement
from models.State import State
from models.brick.Brick import Brick


class App(NamedElement):
    def __init__(self, name: str, initialState: State, states: list[State], bricks :list[Brick] = None):
        super().__init__(name)
        
        self.initialState = initialState
        self.states = states
        
        if (bricks == None) :
            self.bricks = []
        else :
            self.bricks = bricks
    
    def __str__(self) -> str:
        return f"""void setup(){{
\tSerial.begin(9600);
{''.join([str(brick) + "\n" for brick in self.bricks]).rstrip()}
}}

void loop(){{
\t{self.initialState.generateCall()}
}}
{''.join([str(state) + "\n" for state in self.states]).rstrip()}
    """