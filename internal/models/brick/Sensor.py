from Brick import Brick

class Sensor(Brick):
    def __init__(self, name:str, pin: int):
        super().__init__(name,pin)