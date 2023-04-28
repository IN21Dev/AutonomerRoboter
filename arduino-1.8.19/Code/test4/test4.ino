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
    inDat = Wifi.read();
    Serial.println(inDat);
  }

  Serial.println(inDat);
  
  //Zurück senden über Serial 
  if(Serial.available() )
  {
    byte outDat = Serial.read();
    Wifi.write(outDat);
  }

   // Idle que Wert = 106

 if (inDat == 106) {
      Serial.println("Idle Start");
      motor1.stop();
      motor2.stop();
      motor3.stop();
      motor4.stop();
      delay(1000);
      Serial.println("Idle Stop");   
    }

  // Vorwärts Wert = 1 
  
  if (inDat == 1) {
      motor2.run(255);
      motor3.run(-255);
      Serial.println("Vorwärts augefürt");
      delay(2000);
      motor2.stop();
      motor3.stop();
      Serial.println("Vorwärts gestoppt");   
      delay(10000);
    }
    
   // Rückwärts Wert = 2
    
  if (inDat == 2) {
      motor2.run(-255);
      motor3.run(255);
      Serial.println("Rückwärts augefürt");
      delay(2000);
      motor2.stop();
      motor3.stop();
      Serial.println("Rückwärts gestoppt");   
      delay(10000);
  }
  // Drehen Wert = 3
  
  if (inDat == 3) {
      motor2.run(-255);
      motor3.run(-255);
      Serial.println("Drehen augefürt");
      delay(2000);
      motor2.stop();
      motor3.stop();
      Serial.println("Drehen gestoppt");   
      delay(10000);
    }

    // Arm Hoch Wert = 4 

   if (inDat == 4) {
      motor1.run(255);
      Serial.println("Arm Hoch augefürt");
      delay(400);
      motor1.stop();
      Serial.println("Arm Hoch gestoppt");   
      delay(10000);
    }

        // Arm Runter Wert = 5 

   if (inDat == 5) {
      motor1.run(-255);
      Serial.println("Arm Runter augefürt");
      delay(400);
      motor1.stop();
      Serial.println("Arm Runter gestoppt");   
      delay(10000);
    }
  
}
