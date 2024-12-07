#include "init.hpp"
#include "step.hpp"
#include "state.hpp"
#include "digitalAction.hpp"
#include "digitalCondition.hpp"

int main() {
    Init init;
    init.sensor(12);
    init.device(9);
    init.endInit();

    Step step(0);
    DigitalAction action1(9, State::ON);
    DigitalAction action3(7, State::OFF);
    DigitalCondition condition1(12, State::ON, 1);

    step.addDigitalAction(action1);
    step.addDigitalAction(action3);
    step.addDigitalCondition(condition1);
    step.finish();

    Step step2(1);
    DigitalAction action2(9, State::OFF);
    DigitalCondition condition2(12, State::OFF, 0);
    DigitalCondition condition3(11, State::ON, 0);
    step2.addDigitalAction(action2);
    step2.addDigitalCondition(condition2);
    step2.addDigitalCondition(condition3);
    step2.finish();
    
    return 0;
}
