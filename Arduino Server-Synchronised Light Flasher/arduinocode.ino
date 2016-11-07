

void setup()
{
  Serial.begin(9600);
  pinMode(LED_BUILTIN, OUTPUT);
}

void loop()
{
  String value = Serial.readStringUntil('\n');
  if(value == "ON") {
    digitalWrite(LED_BUILTIN, HIGH);
  } else if(value == "OFF") {
    digitalWrite(LED_BUILTIN, LOW);
  }
}
