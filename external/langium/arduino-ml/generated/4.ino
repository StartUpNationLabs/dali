// Generated code for Scenario4

void setup() {
  Serial.begin(9600);
  pinMode(10, INPUT);
  pinMode(9, OUTPUT);
  pinMode(11, OUTPUT);
}

void OffAll() {
    digitalWrite(9, LOW);
    analogWrite(11, 0);
    int front198 = false;

    while (true) {
        if (digitalRead(10) == LOW) {
      front198 = true;
    }

    if (front198 == true && digitalRead(10) == HIGH) {
      OnBuzzer();
    }
    }
  }
void OnBuzzer() {
    analogWrite(11, 800);
    int front298 = false;

    while (true) {
        if (digitalRead(10) == LOW) {
      front298 = true;
    }

    if (front298 == true && digitalRead(10) == HIGH) {
      OnLed();
    }
    }
  }
void OnLed() {
    analogWrite(11, 0);
    digitalWrite(9, HIGH);
    int front411 = false;

    while (true) {
        if (digitalRead(10) == LOW) {
      front411 = true;
    }

    if (front411 == true && digitalRead(10) == HIGH) {
      OffAll();
    }
    }
  }
void loop() {
  OffAll();
}
