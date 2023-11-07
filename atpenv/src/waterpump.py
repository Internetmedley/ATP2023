import water_sensor

class WaterPump:
    def __init__(self):
        pass

    def empty_lock(self, s: water_sensor.WaterLevelSensor) -> water_sensor.WaterLevelState:       #pumps the water away into the ocean
        return s.check_level()