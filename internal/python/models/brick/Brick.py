from models.NamedElement import NamedElement

class Brick(NamedElement):
    def __init__(self, name:str, pin: int):
        super().__init__(name)
        self.pin = pin