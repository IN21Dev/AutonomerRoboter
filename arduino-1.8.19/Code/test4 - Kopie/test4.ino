//Serial lib
#include <SoftwareSerial.h>
//IO Lib
#include "MeMegaPi.h"
//Wifi Lib
#include "MeOrion.h"

#include <Wire.h>

//Wifi Module 
MeWifi Wifi(PORT_8);

//Motor GreiferArm
MeMegaPiDCMotor motor1(PORT1B);

//Motor links
MeMegaPiDCMotor motor2(PORT2B);

//Motor rechts
MeMegaPiDCMotor motor3(PORT3B);

//Motor Greifer
MeMegaPiDCMotor motor4(PORT4B);

void setup()
{
  //Serial und Wifi ini
  Serial.begin(9600);
  Wifi.begin(9600);
  Serial.println("Wifi Start!");

}

void loop()
{
  byte outDat;
  byte inDat;
  
  //Serial empfangen
  if(Wifi.available() )
  {
    byte inDat = Wifi.read();
    Serial.println(inDat);
  }
  
  //Zurück senden über Serial 
  if(Serial.available() )
  {
    byte outDat = Serial.read();
    Wifi.write(outDat);
  }

  // 1 = vorne 
  
  if (inDat == 1) {
      motor2.run(255);
      motor3.run(-255);
      delay(1000);
      motor2.stop();
      motor3.stop();
      Serial.println("Vorwärts augefürt");
    }else {Serial.println("Fail");
          delay (1000);
          }
    
   /* 2 = rück
    
  if (inDat == 2) {
      motor1.run(255);
      delay(5000);
      motor1.stop();
      motor2.stop();
    }
    
  // 3 = drehen
  
  if (inDat == 3) {
      motor1.run(-255);
      motor2.run(-255);
      delay(5000);
      motor1.stop();
      motor2.stop();
    }*/
  
}
