#ifndef STEP_HPP
#define STEP_HPP

#include <vector>

#include "digitalAction.hpp"
#include "digitalCondition.hpp"

class Step {
private:
    std::vector<DigitalAction> _digitalActions;
    std::vector<DigitalCondition> _digitalConditions;

public:
    Step();
    void addDigitalAction(DigitalAction digitalAction);
    void addDigitalCondition(DigitalCondition digitalCondition);
    void finish();
};

#endif
