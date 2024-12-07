// Generated code for Scenario1

void setup() {
  Serial.begin(9600);
  pinMode(10, INPUT);
  pinMode(9, OUTPUT);
  pinMode(11, OUTPUT);
}

void Off() {
    digitalWrite(9, LOW);
    analogWrite(11, 0);
    
    while (true) {
    
    if (digitalRead(10) == HIGH) {
      On();
    }
    }
  }
void On() {
    digitalWrite(9, HIGH);
    analogWrite(11, 800);
    
    while (true) {
    
    if (digitalRead(10) == LOW) {
      Off();
    }
    }
  }
void loop() {
  Off();
}
