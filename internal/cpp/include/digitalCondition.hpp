#ifndef DIGITAL_CONDITION_HPP
#define DIGITAL_CONDITION_HPP

#include <string>
#include "state.hpp"

class DigitalCondition {
private:   
    std::string _stateToString();
    
    

public:
    int pinNumber;
    State state;
    int nextStep;
    

    DigitalCondition(const int &pin, State state, int nextStep);
    std::string getState();    
};

#endif
