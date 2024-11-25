import type { ValidationAcceptor, ValidationChecks } from 'langium';
import type { ArdunioMlAstType, Person } from './generated/ast.js';
import type { ArdunioMlServices } from './ardunio-ml-module.js';

/**
 * Register custom validation checks.
 */
export function registerValidationChecks(services: ArdunioMlServices) {
    const registry = services.validation.ValidationRegistry;
    const validator = services.validation.ArdunioMlValidator;
    const checks: ValidationChecks<ArdunioMlAstType> = {
        Person: validator.checkPersonStartsWithCapital
    };
    registry.register(checks, validator);
}

/**
 * Implementation of custom validations.
 */
export class ArdunioMlValidator {

    checkPersonStartsWithCapital(person: Person, accept: ValidationAcceptor): void {
        if (person.name) {
            const firstChar = person.name.substring(0, 1);
            if (firstChar.toUpperCase() !== firstChar) {
                accept('warning', 'Person name should start with a capital.', { node: person, property: 'name' });
            }
        }
    }

}
