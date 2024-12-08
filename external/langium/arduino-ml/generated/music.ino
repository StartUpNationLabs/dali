// Generated code for SmartHome

void setup() {
  Serial.begin(9600);
  pinMode(8, INPUT);
  pinMode(12, INPUT);
  pinMode(11, OUTPUT);
}

void Idle() {
    analogWrite(11, 0);
    
    
    while (true) {
    
    
    if (digitalRead(8) == HIGH) {
      delay(50);
      Play1();
    }
    if (digitalRead(12) == HIGH) {
      delay(50);
      Play2();
    }
    }
  }
void Play1() {
    tone(11, 330, 400);
    delay(400);
    tone(11, 0, 100);
    delay(100);
    tone(11, 330, 400);
    delay(400);
    tone(11, 0, 100);
    delay(100);
    tone(11, 330, 800);
    delay(800);
    tone(11, 0, 200);
    delay(200);
    tone(11, 330, 400);
    delay(400);
    tone(11, 0, 100);
    delay(100);
    tone(11, 330, 400);
    delay(400);
    tone(11, 0, 100);
    delay(100);
    tone(11, 330, 800);
    delay(800);
    tone(11, 0, 200);
    delay(200);
    tone(11, 330, 400);
    delay(400);
    tone(11, 0, 100);
    delay(100);
    tone(11, 392, 400);
    delay(400);
    tone(11, 0, 100);
    delay(100);
    tone(11, 262, 400);
    delay(400);
    tone(11, 0, 100);
    delay(100);
    tone(11, 294, 400);
    delay(400);
    tone(11, 0, 100);
    delay(100);
    tone(11, 330, 1600);
    delay(1600);
    tone(11, 0, 400);
    delay(400);
    
    while (true) {
    
    if (true) {
      delay(50);
      Idle();
    }
    }
  }
void Play2() {
    tone(11, 349, 400);
    delay(400);
    tone(11, 0, 100);
    delay(100);
    tone(11, 349, 400);
    delay(400);
    tone(11, 0, 100);
    delay(100);
    tone(11, 349, 400);
    delay(400);
    tone(11, 0, 100);
    delay(100);
    tone(11, 349, 400);
    delay(400);
    tone(11, 0, 100);
    delay(100);
    tone(11, 349, 400);
    delay(400);
    tone(11, 0, 100);
    delay(100);
    tone(11, 330, 400);
    delay(400);
    tone(11, 0, 100);
    delay(100);
    tone(11, 330, 400);
    delay(400);
    tone(11, 0, 100);
    delay(100);
    tone(11, 330, 400);
    delay(400);
    tone(11, 0, 100);
    delay(100);
    tone(11, 330, 400);
    delay(400);
    tone(11, 0, 100);
    delay(100);
    tone(11, 294, 400);
    delay(400);
    tone(11, 0, 100);
    delay(100);
    tone(11, 294, 400);
    delay(400);
    tone(11, 0, 100);
    delay(100);
    tone(11, 330, 400);
    delay(400);
    tone(11, 0, 100);
    delay(100);
    tone(11, 294, 800);
    delay(800);
    tone(11, 0, 200);
    delay(200);
    tone(11, 392, 1600);
    delay(1600);
    tone(11, 0, 400);
    delay(400);
    
    while (true) {
    
    if (true) {
      delay(50);
      Idle();
    }
    }
  }
void loop() {
  Idle();
}
