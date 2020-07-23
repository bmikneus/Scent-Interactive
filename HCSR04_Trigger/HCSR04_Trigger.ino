#include <HCSR04.h>

HCSR04 hc(5,6);//initialisation class HCSR04 (trig pin , echo pin)
#define OUTPUT_PIN 13
unsigned long last_time = 0;
int data = 0;
void setup()
{ Serial.begin(9600); 
  Serial.println("start HCRS04 trigger");
  pinMode(OUTPUT_PIN, OUTPUT);
}

void loop()
{ 
  
  if(millis() - last_time < 4000){
    // Do Nothing
    Serial.println(millis());
  }else{
    data = hc.dist();
    Serial.println( data );
    if(data > 0 && data < 50){
      last_time = millis();
      digitalWrite(OUTPUT_PIN, HIGH);
    }else{
      digitalWrite(OUTPUT_PIN, LOW);
    }
  }
  delay(500);
}//return curent distance in serial
