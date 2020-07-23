#define RELAY_PIN 13
#define BUTTON_IN_PIN 2
#define BUTTON_OUT_PIN 7
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  Serial.println("Starting up relay code");
  pinMode(RELAY_PIN, OUTPUT);
  pinMode(BUTTON_IN_PIN, INPUT);
  pinMode(BUTTON_OUT_PIN, OUTPUT);
  digitalWrite(BUTTON_OUT_PIN, HIGH);
}

void loop() {
  // put your main code here, to run repeatedly:
  //int data = digitalRead(BUTTON_IN_PIN);
  digitalWrite(BUTTON_OUT_PIN, HIGH);
  /*if(digitalRead(BUTTON_IN_PIN) == HIGH){
    digitalWrite(RELAY_PIN, HIGH);
    Serial.println("Button Pressed");
  }else{
    digitalWrite(RELAY_PIN, LOW);
    Serial.println("Button NOT Pressed");
  }*/
  delay(500);
}
