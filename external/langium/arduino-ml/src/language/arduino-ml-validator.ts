import {ArduinoMlServices} from "./arduino-ml-module.js";
import {Actuator, App, ArduinoMlAstType, MelodyAction, Sensor} from "./generated/ast.js";
import {ValidationAcceptor, ValidationChecks} from "langium";

/**
 * Register custom validation checks.
 */
export function registerValidationChecks(services: ArduinoMlServices) {
    const registry = services.validation.ValidationRegistry;
    const validator = services.validation.ArduinoMlValidator;
    const checks: ValidationChecks<ArduinoMlAstType> = {
        Actuator: validator.checkActuator,
        Sensor: validator.checkSensor,
        MelodyAction: validator.checkMelodyAction,
        App: validator.checkApp,
    };
    registry.register(checks, validator);
}


/**
 * Implementation of custom validations.
 */
export class ArduinoMlValidator {

    checkActuator(actuator: Actuator, accept: ValidationAcceptor): void {
        // check if the pin is positive or 0
        if (actuator.outputPin < 0) {
            accept('error', 'Actuator pin must be positive.', {node: actuator, property: 'outputPin'});
        }
    }

    checkSensor(sensor: Sensor, accept: ValidationAcceptor): void {
        // check if the pin is positive or 0
        if (sensor.inputPin < 0) {
            accept('error', 'Actuator pin must be positive.', {node: sensor, property: 'inputPin'});
        }
    }

    checkMelodyAction(melodyAction: MelodyAction, accept: ValidationAcceptor): void {
        // check frequency between 31 and 65535 or 0 for no sound
        if ( melodyAction.frequency != 0 && (melodyAction.frequency < 31 || melodyAction.frequency > 65535) ) {
            accept('error', 'Melody action frequency must be between 31 and 65535 or 0 for no sound.', {node: melodyAction, property: 'frequency'});
        }

    }


    checkApp(app: App, accept: ValidationAcceptor): void {
        const bricks = app.bricks;
        // check for unique Brick names
        let brickNames = new Set();
        bricks.forEach(brick => {
            if (brick.name) {
                if (brickNames.has(brick.name)) {
                    accept('error', 'Brick names must be unique.', {node: brick, property: 'name'});
                } else {
                    brickNames.add(brick.name);
                }
            }
        });

    }


}
