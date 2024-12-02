// Generated code for SmartHome

enum State {Idle,Alert,Standby,};

State currentState = Idle;

int lastmotionSensor = 0;
int lastlightSensor = 0;
void setup() {
  Serial.begin(9600);
  pinMode(1, INPUT);
  pinMode(2, INPUT);
  pinMode(3, OUTPUT);
  pinMode(4, OUTPUT);
  pinMode(5, OUTPUT);
  lastmotionSensor = digitalRead(1);
  lastlightSensor = digitalRead(2);
}

void loop() {
  if (currentState == Idle) {
    digitalWrite(3, LOW);
    digitalWrite(4, LOW);
    if ((digitalRead(1) == HIGH and digitalRead(2) == LOW)) {
      currentState = Alert;
      lastmotionSensor = digitalRead(1);
      lastlightSensor = digitalRead(2);
    }
  }
  if (currentState == Alert) {
    digitalWrite(3, HIGH);
    digitalWrite(4, HIGH);
    tone(5, 800, 123);
    delay(123);
    if ((!(digitalRead(1) == HIGH) or digitalRead(2) == HIGH && lastlightSensor == LOW)) {
      currentState = Idle;
      lastmotionSensor = digitalRead(1);
      lastlightSensor = digitalRead(2);
    }
    if (false) {
      currentState = Standby;
      lastmotionSensor = digitalRead(1);
      lastlightSensor = digitalRead(2);
    }
  }
  if (currentState == Standby) {
    digitalWrite(3, LOW);
    digitalWrite(4, HIGH);
    if (true) {
      currentState = Alert;
      lastmotionSensor = digitalRead(1);
      lastlightSensor = digitalRead(2);
    }
  }
}
