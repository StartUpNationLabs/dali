#include <iostream>

#include <vector>
#include "step.hpp"

Step::Step(){
    _digitalActions;
    _digitalConditions;
};

void Step::addDigitalAction(DigitalAction digitalAction){
    _digitalActions.push_back(digitalAction);
}
void Step::addDigitalCondition(DigitalCondition digitalCondition){
    _digitalConditions.push_back(digitalCondition);
}

void Step::finish(){
    for (size_t i = 0; i < _digitalConditions.size(); ++i) {
        std::cout << "  int conditionState"<< i <<";\n";
    }
    for (size_t i = 0; i < _digitalActions.size(); ++i) {
        _digitalActions[i].print();
    }

    std::cout << "  do{\n";
    std::cout << "    delay(20);\n\n";

    for (size_t i = 0; i < _digitalConditions.size(); ++i) {
        std::cout << "    conditionState"<< i << " = digitalRead("<< _digitalConditions[i].pinNumber <<");\n";
        std::cout << "    if(conditionState"<< i <<" == "<< _digitalConditions[i].getState() <<"){\n";
        std::cout << "      step"<< _digitalConditions[i].nextStep <<"();\n";
        std::cout << "    }\n";
    }

    //While
    //finish

    std::cout << "  }\n}\n";
}