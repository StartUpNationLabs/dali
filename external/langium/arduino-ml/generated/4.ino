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
    int front190 = false;

    while (true) {
        if (digitalRead(10) == LOW) {
      front190 = true;
    }

    if (front190 == true && digitalRead(10) == HIGH) {
      OnBuzzer();
    }
    }
  }
void OnBuzzer() {
    analogWrite(11, 800);
    int front290 = false;

    while (true) {
        if (digitalRead(10) == LOW) {
      front290 = true;
    }

    if (front290 == true && digitalRead(10) == HIGH) {
      OnLed();
    }
    }
  }
void OnLed() {
    analogWrite(11, 0);
    digitalWrite(9, HIGH);
    int front403 = false;

    while (true) {
        if (digitalRead(10) == LOW) {
      front403 = true;
    }

    if (front403 == true && digitalRead(10) == HIGH) {
      OffAll();
    }
    }
  }
void loop() {
  OffAll();
}
