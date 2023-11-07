from math import factorial
from typing import List, Callable, TypeVar, NamedTuple, Tuple, Union, Generator
import atplogger as log
import distance_sensor
import watergate as wg
import water_sensor
import unittest
import servo
import boat
import waterpump



class Test1_Bericht_sturen_naar_poorten(unittest.TestCase):
    def test_open_gate(self):
        s = servo.MyServo(53)       #attach to pin 53
        landGate = wg.WaterGate(s)
        state = wg.GateState.CLOSED

        newState = landGate.open_gate(state)                #open the door and save the returned state
        self.assertEqual(newState, wg.GateState.OPEN)       #assert if state has changed


class Test2_Laten_vollopen_en_legen_van_de_suis(unittest.TestCase):
    def test_fill_lock(self):
        s = servo.MyServo(51)       #attach to pin 51
        hatch = wg.WaterGate(s)
        first_hatch_state = wg.GateState.CLOSED
        second_hatch_state = hatch.open_gate(first_hatch_state)

        waterSensor1 = water_sensor.WaterLevelSensor(90)            #measured water level in constructor, sensor1 is the sensor in the lock
        waterSensor2 = water_sensor.WaterLevelSensor(81)            #sensor out at sea
        self.assertEqual(waterSensor1.check_level(), waterSensor2.check_level())
        self.assertEqual(waterSensor1.check_level(), water_sensor.WaterLevelState.HIGH)
        self.assertEqual(waterSensor2.check_level(), water_sensor.WaterLevelState.HIGH)

    def test_empty_lock(self):
        result = 5 - 4
        self.assertEqual(result, 1)

class Test3_Boot_doorlaten(unittest.TestCase):
    def test_from_land_to_water(self):
        b = boat.Boat()
        boatState1 = boat.BoatState.ON_LAND
        boatState2 = b.next_phase_land_to_water(boatState1)
        boatState3 = b.next_phase_land_to_water(boatState2)


        self.assertEqual(boatState1, boat.BoatState.ON_LAND)
        self.assertEqual(boatState2, boat.BoatState.IN_LOCK)
        self.assertEqual(boatState3, boat.BoatState.ON_WATER)


def main():
    ding = distance_sensor.DistanceSensor("dit is een sensor")
    print(ding.getName())

    print(ding.add(1,4))
    


if __name__ == "__main__":
    loader = unittest.TestLoader()
    test1 = loader.loadTestsFromTestCase(Test1_Bericht_sturen_naar_poorten)
    test2 = loader.loadTestsFromTestCase(Test2_Laten_vollopen_en_legen_van_de_suis)
    test3 = loader.loadTestsFromTestCase(Test3_Boot_doorlaten)

    runner = unittest.TextTestRunner()
    result = runner.run(test1)
    log.show_log()
    result = runner.run(test2)
    log.show_log()
    result = runner.run(test3)
    log.show_log()
    
    print("Test run completed.")
