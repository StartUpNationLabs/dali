import type {App, Condition} from '../language/generated/ast.js';
import {toString} from 'langium/generate';
import * as fs from 'node:fs';
import * as path from 'node:path';
import {extractDestinationAndName} from './cli-util.js';


export function generateIno(model: App, filePath: string, destination: string | undefined): string {
    const data = extractDestinationAndName(filePath, destination);
    const generatedFilePath = `${path.join(data.destination, data.name)}.ino`;

    let code = '';

    // Extract app details
    const {name, bricks, initial, states} = model;

    code += `// Generated code for ${name}\n\n`;
    // make an enum for the states
    code += `enum State {`;
    states.forEach(state => {
        code += `${state.name},`;
    });
    code += `};\n\n`;

    // Declare the state variable
    code += `State currentState = ${initial.ref?.name};\n\n`;

    // Declare the variables that store the last state of the sensors
    bricks.forEach(brick => {
        if (brick.$type === 'Sensor') {
            code += `int last${brick.name} = 0;\n`;
        }
    });

    // Declare the setup function
    code += `void setup() {\n`;
    code += `  Serial.begin(9600);\n`;

    // Initialize bricks
    bricks.forEach(brick => {
        if (brick.$type === 'Sensor') {
            code += `  pinMode(${brick.inputPin}, INPUT);\n`;
        }
        if (brick.$type === 'DigitalActuator') {
            code += `  pinMode(${brick.outputPin}, OUTPUT);\n`;
        } else if (brick.$type === 'AnalogActuator') {
            code += `  pinMode(${brick.outputPin}, OUTPUT);\n`;
        }
    });
    // read the initial state of the sensors
    bricks.forEach(brick => {
        if (brick.$type === 'Sensor') {
            code += `  last${brick.name} = digitalRead(${brick.inputPin});\n`;
        }
    });


    code += `}\n\n`;

    // Declare the loop function
    code += `void loop() {\n`;

    // Generate states and transitions
    states.forEach(state => {
        code += `  if (currentState == ${state.name}) {\n`;
        state.actions.forEach(action => {
            if (action.$type === 'DigitalAction') {
                code += `    digitalWrite(${action.actuator.ref?.outputPin}, ${action.value.value});\n`;
            } else if (action.$type === 'AnalogAction') {
                if (action.duration) {
                    code += `    tone(${action.actuator.ref?.outputPin}, ${action.frequency}, ${action.duration});\n`;
                    code += `    delay(${action.duration});\n`;
                } else {
                    code += `    analogWrite(${action.actuator.ref?.outputPin}, ${action.frequency});\n`;
                }
            }
        });

        // Handle transitions

        state.transitions.forEach(transition => {
            code += `    if (${generateConditionCode(transition.condition)}) {\n`;
            code += `      currentState = ${transition.next.ref?.name};\n`;
            bricks.forEach(brick => {
                if (brick.$type === 'Sensor') {
                    code += `      last${brick.name} = digitalRead(${brick.inputPin});\n`;
                }
            });
            code += `    }\n`;
        });

        code += `  }\n`;
    });

    code += `}\n`;


    if (!fs.existsSync(data.destination)) {
        fs.mkdirSync(data.destination, {recursive: true});
    }
    fs.writeFileSync(generatedFilePath, toString(code));
    return generatedFilePath;
}


function generateConditionCode(condition: Condition): string {
    if (condition.$type === 'LogicalOperator') {
        return `(${generateConditionCode(condition.left)} ${condition.type} ${generateConditionCode(condition.right)})`;
    } else if (condition.$type === 'Not') {
        return `!(${generateConditionCode(condition.value)})`;
    }
    if (condition.$type === 'Simple') {
        return `digitalRead(${condition.sensor.ref?.inputPin}) == ${condition.value.value}`;
    } else if (condition.$type === 'Change') {
        // get the last value of the sensor and compare it with the current value
        // condition.value dictate if it is a rise or a decrease
        if (condition.value.value === 'HIGH') {
            return `digitalRead(${condition.sensor.ref?.inputPin}) == HIGH && last${condition.sensor.ref?.name} == LOW`;
        } else if (condition.value.value === 'LOW') {
            return `digitalRead(${condition.sensor.ref?.inputPin}) == LOW && last${condition.sensor.ref?.name} == HIGH`;
        }

    } else if (condition.$type === 'Constant') {
        return condition.value;
    }
    return '';
}