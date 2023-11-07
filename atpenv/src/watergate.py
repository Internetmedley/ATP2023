from enum import Enum
import servo
from atplogger import log_arguments


class GateState(Enum):
    OPEN=1
    CLOSED=2

class WaterGate():
    def __init__(self, s: servo.MyServo):
        self.motor = s
        return

    @log_arguments
    def open_gate(self, state: GateState) -> GateState:
        if(state == GateState.OPEN):
            self.motor.write(180)               #imagine 180 is closed
            return GateState.CLOSED
        else:
            self.motor.write(0)                 #imagine 0 is open
            return GateState.OPEN

    @log_arguments
    def close_gate(self, state: GateState) -> GateState:
        if(state == GateState.CLOSED):
            self.motor.write(180)
            return GateState.OPEN
        else:
            self.motor.write(0)
            return GateState.CLOSED
