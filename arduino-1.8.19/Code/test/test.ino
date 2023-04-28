#include <SoftwareSerial.h>
#include "MeMegaPi.h"
#include "MeOrion.h"


MeWifi Wifi(PORT_6);


MeMegaPiDCMotor motor1(PORT1B);

MeMegaPiDCMotor motor2(PORT2B);

MeMegaPiDCMotor motor3(PORT3B);

MeMegaPiDCMotor motor4(PORT4B);

uint8_t motorSpeed = 255;
uint8_t motorSpeed1 = -100;

void setup()
{
  Serial.begin(9600);
  Wifi.begin(9600);
  Serial.println("Wifi Start!");
  motor3.run(-100);

}

void loop()
{
  char inDat;
  char outDat;
  if(Wifi.available() )
  {
    char c = Wifi.read();
    Serial.print(c);
  }
  if(Serial.available() )
  {
    outDat = Serial.read();
    Wifi.write(outDat);
  }
  
}
