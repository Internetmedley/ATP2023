from enum import Enum
from atplogger import log_arguments

class WaterLevelState(Enum):
    HIGH=1
    MID=2
    LOW=3

class WaterLevelSensor:
    def __init__(self, val: int):
        self.level = val
        return

    def read(self) -> int:
        return self.level

    @log_arguments
    def check_level(self) -> WaterLevelState:
        if (self.read() >= 80):
            return WaterLevelState.HIGH
        elif(self.read() >=10):
            return WaterLevelState.MID
        else:
            return WaterLevelState.LOW

