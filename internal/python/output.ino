int button = 0;
int led = 1;
int buzzer = 2;

void setup(){
	Serial.begin(9600);
	pinMode(button, INPUT);
	pinMode(led, OUTPUT);
	pinMode(buzzer, OUTPUT);
}

void loop(){
	state1();
}

void state1(){
	digitalWrite(led,HIGH);
    
	while(true){
		if(false){
			state2();
		}
		
		if(!false){
			state2();
		}
		
		if((digitalRead(button) == HIGH) && !false){
			state2();
		}
	}
}


void state2(){
	tone(buzzer, 120, 5);
	delay(5);
    
	while(true){
	}
}
    
