// Generated code for Scenario3

enum State {Off,On,};

State currentState = Off;

int lastbutton = 0;
void setup() {
  Serial.begin(9600);
  pinMode(10, INPUT);
  pinMode(9, OUTPUT);
  lastbutton = digitalRead(10);
}

void loop() {
  if (currentState == Off) {
    digitalWrite(9, LOW);
    if (digitalRead(10) == HIGH && lastbutton == LOW) {
      currentState = On;
      lastbutton = digitalRead(10);
    }
  }
  if (currentState == On) {
    digitalWrite(9, HIGH);
    if (digitalRead(10) == HIGH && lastbutton == LOW) {
      currentState = Off;
      lastbutton = digitalRead(10);
    }
  }
}
