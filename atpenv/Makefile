### Makefile for ATP 
### Author: Remy de Bruijn
### 06-11-2023
### This Makefile makes a shared object for making a bind between c++ and python with pybind11 
### and also runs the program.
### build .so manually with: $ c++ -O3 -Wall -shared -std=c++11 -fPIC $(python3 -m pybind11 --includes) example.cpp -o example$(python3-config --extension-suffix)


ENV_PATH := ~/ATP/atpenv
PYTHON_PATH := $(ENV_PATH)/bin/python3
SRC_PATH := $(ENV_PATH)/src
CXX := g++  
CXXFLAGS := -O3 -Wall -shared -std=c++11 -fPIC
PYTHON_INCLUDE := $(shell python3 -m pybind11 --includes)
PYTHON_EXTENSION_SUFFIX := $(shell python3-config --extension-suffix)
SRCS := $(wildcard $(SRC_PATH)/*.cpp)
HDRS := $(wildcard $(SRC_PATH)/*.h)
#OBJS := $(patsubst $(SRC_PATH)/%.cpp, %.o, $(SRCS))
TARGET := $(SRC_PATH)/distance_sensor$(PYTHON_EXTENSION_SUFFIX)
PYTHON_SCRIPT := $(SRC_PATH)/main.py

all: $(TARGET)

$(TARGET): $(SRCS) $(HDRS)
	$(CXX) $(CXXFLAGS) $(PYTHON_INCLUDE) $^ -o $@

%.o: $(SRC_PATH)/%.cpp
	$(CXX) $(CXXFLAGS) $(PYTHON_INCLUDE) -c $< -o $@

run: $(TARGET)
	$(PYTHON_PATH) $(PYTHON_SCRIPT)

clean:
	rm -f $(TARGET)

.PHONY: all clean