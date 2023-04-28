//Serial lib
#include <SoftwareSerial.h>
//IO Lib
#include "MeMegaPi.h"
//Wifi Lib
#include "MeOrion.h"

MeMegaPiDCMotor motor1(PORT1B);

MeMegaPiDCMotor motor2(PORT2B);

MeMegaPiDCMotor motor3(PORT3B);

MeMegaPiDCMotor motor4(PORT4B);

uint8_t motorSpeed = 100;
uint8_t motorSpeed1 = -100;

void setup()
{
  
  motor1.run(motorSpeed);
  motor2.run(motorSpeed);
  motor3.run(motorSpeed);
  motor4.run(motorSpeed);

}

void loop()
{
  
}
