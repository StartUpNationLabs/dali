#ifndef DIGITAL_ACTION_HPP
#define DIGITAL_ACTION_HPP

#include <string>
#include "state.hpp"

class DigitalAction {
private:   
   

    std::string _stateToString();

public:
    int _pinNumber;
    State _state;

    DigitalAction(const int &number, State state);
    const void print();
    
};

#endif
