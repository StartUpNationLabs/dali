// Generated code for Scenario2

enum State {Off,On,};

State currentState = Off;

int lastbutton1 = 0;
int lastbutton2 = 0;
void setup() {
  Serial.begin(9600);
  pinMode(10, INPUT);
  pinMode(12, INPUT);
  pinMode(11, OUTPUT);
  lastbutton1 = digitalRead(10);
  lastbutton2 = digitalRead(12);
}

void loop() {
  if (currentState == Off) {
    analogWrite(11, 0);
    if ((digitalRead(10) == HIGH and digitalRead(12) == HIGH)) {
      currentState = On;
      lastbutton1 = digitalRead(10);
      lastbutton2 = digitalRead(12);
    }
  }
  if (currentState == On) {
    analogWrite(11, 800);
    if ((digitalRead(10) == LOW and digitalRead(12) == LOW)) {
      currentState = Off;
      lastbutton1 = digitalRead(10);
      lastbutton2 = digitalRead(12);
    }
  }
}
