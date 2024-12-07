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
    (DigitalActuator | Buzzer);

DigitalActuator:
	'DigitalActuator' name=ID ':' outputPin=INT;
Buzzer:
    'Buzzer' name=ID ':' outputPin=INT;

State :
	name=ID '{'
		actions+=Action
		(actions+=Action)*
		transitions+=Transition
        (transitions+=Transition)*
	'}';

Action :
    (DigitalAction | MelodyAction);

DigitalAction:
	actuator=[DigitalActuator:ID] '<=' value=Signal;
MelodyAction:
    actuator=[Buzzer:ID] '<=' frequency=INT 'Hz' ( 'for' duration=INT 'milliseconds') ?;

Transition :
	'when' condition=Condition '=>' next=[State:ID];

Condition :
	(LogicalOperator | Not | Comparison | Constant | '(' Condition ')' | Click );

Click:
    sensor=[Sensor:ID] 'clicked';

LogicalOperator:
    '(' left=Condition  type=('and' | 'or') right=Condition ')';

Not:
    'not' '(' value=Condition ')';

Comparison :
    (Simple | Edge);
Simple:
	sensor=[Sensor:ID] 'is' value=Signal;

Edge:
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
hidden terminal ML_COMMENT: /\/\*[\s\S]*?\*\//;
hidden terminal SL_COMMENT: /\/\/[^\n\r]*/;
