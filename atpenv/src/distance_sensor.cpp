#include <pybind11/pybind11.h>
//#include "Adafruit_VL53L0X.h"


//Adafruit_VL53L0X lox = Adafruit_VL53L0X();
namespace py = pybind11;

//enum class state_t{}

class DistanceSensor{
    int val;

    public:
    DistanceSensor(const int &val) : val(val) 
    {}

    const int &get_value() const { return val; }

    // int add(int a, int b) {
    //     return a + b;
    // }
};


PYBIND11_MODULE(distance_sensor, m) {
    py::class_<DistanceSensor>(m, "DistanceSensor")
         .def(py::init<const int &>())
        .def("get_value", &DistanceSensor::get_value);
}