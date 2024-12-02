int led = 9; 
int buzzer = 11;
int button= 10;

void setup() {
  pinMode(led, OUTPUT); 
  pinMode(buzzer, OUTPUT); 
  pinMode(button, INPUT);

  state0();
}

void loop() {
  state0();
}

void state0() {
  int buttonState;
  digitalWrite(led, LOW);
  digitalWrite(buzzer, LOW);
  do{
    delay(20);
    buttonState = digitalRead(button);
  }while(buttonState == LOW);
  state1();
}

void state1() {
  int buttonState;
  digitalWrite(led, HIGH);
  digitalWrite(buzzer, HIGH);
  do{
    delay(20);
    buttonState = digitalRead(button);
  }while(buttonState == HIGH);
  state0();
}