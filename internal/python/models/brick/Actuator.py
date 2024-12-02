from models.brick.Brick import Brick

class Actuator(Brick):
    def __init__(self, name: str, pin: int):
        super().__init__(name,pin)
    
    def __str__(self) -> str:
        return f'pinMode({self.name}, OUTPUT);'