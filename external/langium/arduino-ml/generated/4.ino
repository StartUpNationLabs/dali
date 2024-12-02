// Generated code for Scenario4

enum State {OffAll,OnBuzzer,OnLed,};

State currentState = OffAll;

int lastbutton = 0;
void setup() {
  Serial.begin(9600);
  pinMode(10, INPUT);
  pinMode(9, OUTPUT);
  pinMode(11, OUTPUT);
  lastbutton = digitalRead(10);
}

void loop() {
  if (currentState == OffAll) {
    digitalWrite(9, LOW);
    analogWrite(11, 0);
    if (digitalRead(10) == HIGH && lastbutton == LOW) {
      currentState = OnBuzzer;
      lastbutton = digitalRead(10);
    }
  }
  if (currentState == OnBuzzer) {
    analogWrite(11, 800);
    if (digitalRead(10) == HIGH && lastbutton == LOW) {
      currentState = OnLed;
      lastbutton = digitalRead(10);
    }
  }
  if (currentState == OnLed) {
    analogWrite(11, 0);
    digitalWrite(9, HIGH);
    if (digitalRead(10) == HIGH && lastbutton == LOW) {
      currentState = OffAll;
      lastbutton = digitalRead(10);
    }
  }
}
