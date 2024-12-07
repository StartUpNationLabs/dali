from models.condition.Condition import Condition
from typing import Callable

class Transition():
    def __init__(self, nextStateCall: Callable, condition: Condition):
        self.nextStateCall = nextStateCall
        self.condition = condition
    
    def __str__(self) -> str :
        return f"""
\t\tif({str(self.condition)}){{
\t\t\t{self.nextStateCall()}
\t\t}}"""