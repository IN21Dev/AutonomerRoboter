#include <SoftwareSerial.h>
#include <Wire.h>
#include <Makeblock.h>
#include <Arduino.h>

MeWifi Wifi(PORT_8);
void setup()
{
 Serial.begin(9600);
 Wifi.begin(9600);
 Serial.println("Bluetooth Start!");
}
void loop()
{
 char inDat;
 char outDat;
 if(Wifi.available())
 {
 char c = Wifi.read();
 Serial.print(c);

 }
 if(Serial.available())
 {
 outDat = Serial.read();
 Wifi.write(outDat);
 }
}
