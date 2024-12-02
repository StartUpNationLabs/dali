// Generated code for Scenario3

enum State {OffAll,OnAll,OnLed,OffLed,};

State currentState = OffAll;

int lastbutton = 0;
void setup() {
  Serial.begin(9600);
  pinMode(10, INPUT);
  pinMode(9, OUTPUT);
  lastbutton = digitalRead(10);
}

void loop() {
  if (currentState == OffAll) {
    digitalWrite(9, LOW);
    if (digitalRead(10) == HIGH) {
      currentState = OnAll;
      lastbutton = digitalRead(10);
    }
  }
  if (currentState == OnAll) {
    digitalWrite(9, HIGH);
    if (digitalRead(10) == LOW) {
      currentState = OnLed;
      lastbutton = digitalRead(10);
    }
  }
  if (currentState == OnLed) {
    digitalWrite(9, HIGH);
    if (digitalRead(10) == HIGH) {
      currentState = OffLed;
      lastbutton = digitalRead(10);
    }
  }
  if (currentState == OffLed) {
    digitalWrite(9, LOW);
    if (digitalRead(10) == LOW) {
      currentState = OffAll;
      lastbutton = digitalRead(10);
    }
  }
}
