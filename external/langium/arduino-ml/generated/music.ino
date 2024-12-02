// Generated code for SmartHome

enum State {Idle,Play1,Play2,};

State currentState = Idle;

int lastbutton1 = 0;
int lastbutton2 = 0;
void setup() {
  Serial.begin(9600);
  pinMode(8, INPUT);
  pinMode(12, INPUT);
  pinMode(11, OUTPUT);
  lastbutton1 = digitalRead(8);
  lastbutton2 = digitalRead(12);
}

void loop() {
  if (currentState == Idle) {
    analogWrite(11, 0);
    if (digitalRead(8) == HIGH) {
      currentState = Play1;
      lastbutton1 = digitalRead(8);
      lastbutton2 = digitalRead(12);
    }
    if (digitalRead(12) == HIGH) {
      currentState = Play2;
      lastbutton1 = digitalRead(8);
      lastbutton2 = digitalRead(12);
    }
  }
  if (currentState == Play1) {
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
    if (true) {
      currentState = Idle;
      lastbutton1 = digitalRead(8);
      lastbutton2 = digitalRead(12);
    }
  }
  if (currentState == Play2) {
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
    if (true) {
      currentState = Idle;
      lastbutton1 = digitalRead(8);
      lastbutton2 = digitalRead(12);
    }
  }
}
