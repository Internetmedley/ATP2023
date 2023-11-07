from enum import Enum
from atplogger import log_arguments


class BoatState(Enum):
    ON_LAND=1
    IN_LOCK=2
    ON_WATER=3

class Boat:
    def __init__(self):
        pass

    def next_phase_land_to_water(self, state: BoatState):
        if(state == BoatState.ON_LAND):
            return BoatState.IN_LOCK
        elif(state == BoatState.IN_LOCK):
            return BoatState.ON_WATER
        else:
            return state

