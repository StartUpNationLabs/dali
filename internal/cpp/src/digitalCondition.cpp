#include <iostream>
#include "state.hpp"
#include "step.hpp"
#include "digitalCondition.hpp"

DigitalCondition::DigitalCondition(const int &pin, State state, int nextStep) 
    : pinNumber(pin), state(state), nextStep(nextStep){
    // Constructor body (if needed)
}

std::string DigitalCondition::_stateToString(){
    switch (state) {
        case State::ON: return "HIGH";
        case State::OFF: return "LOW";
    }
    exit(1);
}

std::string DigitalCondition::getState(){
    return _stateToString();
}
