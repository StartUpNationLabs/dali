#include "init.hpp"
#include "step.hpp"
#include "state.hpp"
#include "digitalAction.hpp"
#include "digitalCondition.hpp"

#define INIT int main() { Init init;
#define END_INIT init.endInit();
#define END return 0; }

#define ON State::ON
#define OFF State::OFF

#define SENSOR(pin)  init.sensor(pin);
#define DEVICE(pin)  init.device(pin);

#define ACTION(actionNumber, pin, wantedState) DigitalAction action##actionNumber(pin, wantedState);
#define CONDITION(conditionNumber, pin, stateToSwitch, nextStep) DigitalCondition condition##conditionNumber(pin, stateToSwitch, nextStep);

#define STEP(stepNumber) Step step##stepNumber;
#define ADD_CONDITION(stepNumber, conditionNumber) step##stepNumber.addDigitalCondition(condition##conditionNumber);
#define ADD_ACTION(stepNumber, actionNumber) step##stepNumber.addDigitalAction(action##actionNumber);
#define END_STEP(stepNumber) step##stepNumber.finish();