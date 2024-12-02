from ..NamedElement import NamedElement

class Brick(NamedElement):
    def __init__(self, name:str, pin: int):
        super().__init__(name)
        self.pin = pin
    
    def globalVariable(self) -> str :
        return f'{self.name} = {self.pin};'