from models.comparison.Comparison import Comparison
from models.brick.Sensor import Sensor
from models.Signal import Signal
from models.condition.Operator import Operator

class EdgeComparison(Comparison):
    def __init__(self, sensor: Sensor, fromValue: Signal, toValue: Signal):
        super().__init__(sensor)
        self.fromValue = fromValue
        self.toValue = toValue
    
    def flagNeeded(self) -> bool : 
        return True
    
    def generateFlagDefinition(self, offset: str) -> str :
        return f"\tbool flag{self.sensor.name+str(self.sensor.pin)+offset} = false;"
    
    def generateFlagCheck(self, offset: str) -> str :
        return f"""
\t\tif(digitalRead({self.sensor.pin}) == {self.fromValue.value}){{
\t\t\tflag{self.sensor.name+str(self.sensor.pin)+offset} = true;
\t\t}}"""

    def generateCondition(self, offset: str) -> str :
        return f'(flag{self.sensor.name+str(self.sensor.pin)+offset} == true {Operator.AND.value} digitalRead({self.sensor.pin} == {self.toValue.value})'
    
    def __str__(self) -> str :
        return f'(last{self.sensor.name+str(self.sensor.pin)} == {self.fromValue.value} {Operator.AND.value} (last{self.sensor.name+str(self.sensor.pin)} = digitalRead({self.sensor.pin})) == {self.toValue.value})'