int led = 9;
int button= 10;

void setup() {
  pinMode(led, OUTPUT); 
  pinMode(button, INPUT);
}

void loop() {
  state0();
}

void state0() {
  int buttonState;
  digitalWrite(led, LOW);
  do{
    delay(20);
    buttonState = digitalRead(button);
    if(buttonState == LOW){
      state1();
    }
  }while(true);
}

void state1() {
  int buttonState;
  digitalWrite(led, HIGH);
  do{
    delay(20);
    buttonState = digitalRead(button);
  }while(buttonState == HIGH);
  state2();
}

void state2() {
  int buttonState;
  do{
    delay(20);
    buttonState = digitalRead(button);
  }while(buttonState == LOW);
  state3();
}

void state3() {
  int buttonState;
  digitalWrite(led, LOW);
  do{
    delay(20);
    buttonState = digitalRead(button);
  }while(buttonState == HIGH);
  state0();
}
