// Generated code for Scenario1

enum State {Off,On,};

State currentState = Off;

int lastbutton = 0;
void setup() {
  Serial.begin(9600);
  pinMode(10, INPUT);
  pinMode(9, OUTPUT);
  pinMode(11, OUTPUT);
  lastbutton = digitalRead(10);
}

void loop() {
  if (currentState == Off) {
    digitalWrite(9, LOW);
    analogWrite(11, 0);
    if (digitalRead(10) == HIGH) {
      currentState = On;
      lastbutton = digitalRead(10);
    }
  }
  if (currentState == On) {
    digitalWrite(9, HIGH);
    analogWrite(11, 800);
    if (digitalRead(10) == LOW) {
      currentState = Off;
      lastbutton = digitalRead(10);
    }
  }
}
