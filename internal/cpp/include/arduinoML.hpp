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

#define ACTION(number, pin, state) DigitalAction action##number(pin, state);
#define CONDITION(number, pin, state, next_step) DigitalCondition condition##number(pin, state, next_step);

#define STEP(number) Step step##number;
#define ADD_CONDITION(stepNumber, conditionNumber) step##stepNumber.addDigitalCondition(condition##conditionNumber);
#define ADD_ACTION(stepNumber, actionNumber) step##stepNumber.addDigitalAction(action##actionNumber);
#define END_STEP(number) step##number.finish();