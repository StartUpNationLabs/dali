// Generated code for Scenario3

void setup() {
  Serial.begin(9600);
  pinMode(10, INPUT);
  pinMode(9, OUTPUT);
}

void Off() {
    digitalWrite(9, LOW);
    int front136 = false;

    while (true) {
        if (digitalRead(10) == LOW) {
      front136 = true;
    }

    if (front136 == true && digitalRead(10) == HIGH) {
      delay(50);
      On();
    }
    }
  }
void On() {
    digitalWrite(9, HIGH);
    int front211 = false;

    while (true) {
        if (digitalRead(10) == LOW) {
      front211 = true;
    }

    if (front211 == true && digitalRead(10) == HIGH) {
      delay(50);
      Off();
    }
    }
  }
void loop() {
  Off();
}
