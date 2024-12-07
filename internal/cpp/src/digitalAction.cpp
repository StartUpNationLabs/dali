#include <iostream>
#include "state.hpp"
#include "digitalAction.hpp"

DigitalAction::DigitalAction(const int &pin, State state) 
    : _pinNumber(pin), _state(state) {
    // Constructor body (if needed)
}

const void DigitalAction::print(){
    std::cout << "  digitalWrite("<< _pinNumber << ", "<< _stateToString() <<");\n";
}

std::string DigitalAction::_stateToString(){
    switch (_state) {
        case State::ON: return "HIGH";
        case State::OFF: return "LOW";
    }
    exit(1);
}
