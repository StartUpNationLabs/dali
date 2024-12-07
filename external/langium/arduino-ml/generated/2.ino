// Generated code for Scenario2

void setup() {
  Serial.begin(9600);
  pinMode(10, INPUT);
  pinMode(12, INPUT);
  pinMode(11, OUTPUT);
}

void Off() {
    analogWrite(11, 0);
     ;  
    while (true) {
     ;  
    if ((digitalRead(10) == HIGH and digitalRead(12) == HIGH)) {
      On();
    }
    }
  }
void On() {
    analogWrite(11, 800);
     ;  
    while (true) {
     ;  
    if ((digitalRead(10) == LOW or digitalRead(12) == LOW)) {
      Off();
    }
    }
  }
void loop() {
  Off();
}
