int buzzer = 11;
int button1= 10;
int button2= 12;

void setup() {
  pinMode(buzzer, OUTPUT); 
  pinMode(button1, INPUT);
  pinMode(button2, INPUT);
}

void loop() {
  state0();
}

void state0() {
  int buttonState1;
  int buttonState2;
  digitalWrite(buzzer, LOW);
  do{
    delay(20);
    buttonState1 = digitalRead(button1);
    buttonState2 = digitalRead(button2);
    if(buttonState1 == LOW || buttonState2 == LOW){
      state1();
    }
  }while(true);
}

void state1() {
  int buttonState1;
  int buttonState2;
  digitalWrite(buzzer, HIGH);
  do{
    delay(20);
    buttonState1 = digitalRead(button1);
    buttonState2 = digitalRead(button2);
    if(buttonState1 == HIGH && buttonState2 == HIGH){
      state0();
    }
  }while(true);
}
