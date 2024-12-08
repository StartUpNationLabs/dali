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
      delay(50);
      Alert();
    }
    }
  }
void Alert() {
    digitalWrite(3, HIGH);
    digitalWrite(4, HIGH);
    tone(5, 800, 123);
    delay(123);
     ;  int front474 = false;

    
    while (true) {
     ;      if (digitalRead(2) == LOW) {
      front474 = true;
    }

    
    if ((!(digitalRead(1) == HIGH) or front474 == true && digitalRead(2) == HIGH)) {
      delay(50);
      Idle();
    }
    if (false) {
      delay(50);
      Standby();
    }
    }
  }
void Standby() {
    digitalWrite(3, LOW);
    digitalWrite(4, HIGH);
    
    while (true) {
    
    if (true) {
      delay(50);
      Alert();
    }
    }
  }
void loop() {
  Idle();
}
