# Minimum CMake version
cmake_minimum_required(VERSION 3.10)

# Project name and version
project(generate VERSION 1.0)

# Set C++ standard
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED True)

# Add include directory
include_directories(include)

# Glob all source files
file(GLOB SOURCES src/*.cpp main.cpp)
file(GLOB HEADERS include/*.hpp)

# Define the executable
add_executable(${PROJECT_NAME} ${SOURCES} ${HEADERS})
