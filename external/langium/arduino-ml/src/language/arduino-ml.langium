grammar ArduinoMl

entry App:
	'app' name=ID 'initial' 'state' initial=[State:ID]
	'{'

		bricks+=Brick
		(bricks+=Brick)*


		states+=State
		(states+=State)*
	'}';

Brick :
	(Sensor | Actuator);

Sensor :
	'Sensor' name=ID ':' inputPin=INT;

Actuator :
    (DigitalActuator | AnalogActuator);

DigitalActuator:
	'DigitalActuator' name=ID ':' outputPin=INT;
AnalogActuator:
    'AnalogActuator' name=ID ':' outputPin=INT;

State :
	name=ID '{'
		actions+=Action
		(actions+=Action)*
		transition+=Transition
        (Transition+=Transition)*
	'}';

Action :
    (DigitalAction | AnalogAction);

DigitalAction:
	actuator=[DigitalActuator:ID] '<=' value=Signal;
AnalogAction:
    actuator=[AnalogActuator:ID] '<=' frequency=INT 'Hz' ( 'for' duration=INT 'milliseconds') ?;

Transition :
	'when' condition=Condition '=>' next=[State:ID];

Condition :
	(LogicalOperator | Not | Comparison | Constant);

LogicalOperator:
    '(' left=Condition  type=('and' | 'or') right=Condition ')';

Not:
    'not' '(' value=Condition ')';

Comparison :
    (Simple | Change);
Simple:
	sensor=[Sensor:ID] 'is' value=Signal;

Change:
    sensor=[Sensor:ID] 'changed' 'to' value=Signal;

Signal:
	value=(HIGH | LOW);

Constant:
    value=('true' | 'false');

terminal HIGH : 'HIGH';
terminal LOW : 'LOW';

hidden terminal WS: /\s+/;
terminal ID: /[_a-zA-Z][\w_]*/;
terminal INT returns number: /[0-9]+/;
terminal STRING: /"[^"]*"|'[^']*'/;
hidden terminal ML_COMMENT: /\/\*[\s\S]*?\*\//;
hidden terminal SL_COMMENT: /\/\/[^\n\r]*/;
