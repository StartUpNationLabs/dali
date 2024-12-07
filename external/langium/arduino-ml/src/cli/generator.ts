import type {App, Condition} from '../language/generated/ast.js';
import {toString} from 'langium/generate';
import * as fs from 'node:fs';
import * as path from 'node:path';
import {extractDestinationAndName} from './cli-util.js';

function invertSignalValue(value: string): string {
    return value === 'HIGH' ? 'LOW' : 'HIGH';
}


function conditionId(condition: Condition) {
    return condition.$cstNode?.offset;

}


export function generateIno(model: App, filePath: string, destination: string | undefined): string {
    const data = extractDestinationAndName(filePath, destination);
    const generatedFilePath = `${path.join(data.destination, data.name)}.ino`;

    let code = '';

    // Extract app details
    const {name, bricks, initial, states} = model;

    code += `// Generated code for ${name}\n\n`;

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
        } else if (brick.$type === 'Buzzer') {
            code += `  pinMode(${brick.outputPin}, OUTPUT);\n`;
        }
    });


    code += `}\n\n`;


    // Generate states
    states.forEach(state => {
        code += `void ${state.name}() {\n`;
        state.actions.forEach(action => {
            if (action.$type === 'DigitalAction') {
                code += `    digitalWrite(${action.actuator.ref?.outputPin}, ${action.value.value});\n`;
            } else if (action.$type === 'MelodyAction') {
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
            code += `    ${generateStartConditionCode(transition.condition)}\n`;
        })

        code += `    while (true) {\n`;
        state.transitions.forEach(transition => {
            code += `    ${generateStartOfLoopConditionCode(transition.condition)}\n`;
        })

        state.transitions.forEach(transition => {
            code += `    if (${generateConditionCode(transition.condition)}) {\n`;
            code += `      ${transition.next.ref?.name}();\n`;
            code += `    }\n`;
        });
        code += `    }\n`;

        code += `  }\n`;
    });
    // Declare the loop function
    code += `void loop() {\n`;
    code += `  ${initial.ref?.name}();\n`;
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
    } else if (condition.$type === 'Edge') {
        // get the last value of the sensor and compare it with the current value
        // condition.value dictate if it is a rise or a decrease
        return `front${conditionId(condition)} == true && digitalRead(${condition.sensor.ref?.inputPin}) == ${condition.value.value}`;

    } else if (condition.$type === 'Constant') {
        return condition.value;
    } else if (condition.$type === 'Click') {
        return `front${conditionId(condition)} == true && digitalRead(${condition.sensor.ref?.inputPin}) == HIGH`;
    }
    return '';
}

function generateStartConditionCode(condition: Condition): string {
    if (condition.$type === 'LogicalOperator') {
        return `${generateStartConditionCode(condition.left)} ;  ${generateStartConditionCode(condition.right)}`;
    } else if (condition.$type === 'Not') {
        return `${generateStartConditionCode(condition.value)}`;
    }

    if (condition.$type === 'Edge' || condition.$type === 'Click') {
        return `int front${conditionId(condition)} = false;\n`;
    }
    return '';
}

function generateStartOfLoopConditionCode(condition: Condition): string {
    if (condition.$type === 'LogicalOperator') {
        return `${generateStartOfLoopConditionCode(condition.left)} ;  ${generateStartOfLoopConditionCode(condition.right)}`;
    } else if (condition.$type === 'Not') {
        return `${generateStartOfLoopConditionCode(condition.value)}`;
    }
    let code: string = '';

    if (condition.$type === 'Edge') {
        if ("sensor" in condition) {
            code += `    if (digitalRead(${condition.sensor.ref?.inputPin}) == ${invertSignalValue(condition.value.value)}) {\n`;
            code += `      front${conditionId(condition)} = true;\n`;
            code += `    }\n`;
        }
    }

    if (condition.$type === 'Click') {
        if ("sensor" in condition) {
            code += `    if (digitalRead(${condition.sensor.ref?.inputPin}) == LOW) {\n`;
            code += `      front${conditionId(condition)} = true;\n`;
            code += `    }\n`;
        }
    }
    return code;
}