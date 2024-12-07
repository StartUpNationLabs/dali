// Generated code for SmartHome

void setup() {
  Serial.begin(9600);
  pinMode(1, INPUT);
  pinMode(2, INPUT);
  pinMode(3, OUTPUT);
  pinMode(4, OUTPUT);
  pinMode(5, OUTPUT);
}

void Idle() {
    digitalWrite(3, LOW);
    digitalWrite(4, LOW);
     ;  
    while (true) {
     ;  
    if ((digitalRead(1) == HIGH and digitalRead(2) == LOW)) {
      Alert();
    }
    }
  }
void Alert() {
    digitalWrite(3, HIGH);
    digitalWrite(4, HIGH);
    tone(5, 800, 123);
    delay(123);
     ;  int front482 = false;

    
    while (true) {
     ;      if (digitalRead(2) == LOW) {
      front482 = true;
    }

    
    if ((!(digitalRead(1) == HIGH) or front482 == true && digitalRead(2) == HIGH)) {
      Idle();
    }
    if (false) {
      Standby();
    }
    }
  }
void Standby() {
    digitalWrite(3, LOW);
    digitalWrite(4, HIGH);
    
    while (true) {
    
    if (true) {
      Alert();
    }
    }
  }
void loop() {
  Idle();
}
