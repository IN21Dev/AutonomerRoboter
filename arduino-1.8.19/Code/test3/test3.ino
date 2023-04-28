//Serial lib
#include <SoftwareSerial.h>
//IO Lib
#include "MeMegaPi.h"
//Wifi Lib
#include "MeOrion.h"

//Wifi Module 
MeWifi Wifi(PORT_8);

//Motor rechts 
MeMegaPiDCMotor motor1(PORT1B);

//Motor links
MeMegaPiDCMotor motor2(PORT2B);

//Motor GreiferArm
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
  char outDat;
  char inDat;
  
  //Serial empfangen
  if(Wifi.available() )
  {
    //char c = Wifi.read();
    char inDat = Wifi.read();
    Serial.print(inDat);
  }
  
  //Zurück senden über Serial 
  if(Serial.available() )
  {
    outDat = Serial.read();
    Wifi.write(outDat);
  }

  // a = vorne 
  
  //char text[] = "a";
  if (strcmp(&inDat, text) == 0) {
      motor1.run(255);
      motor2.run(255);
      delay(5000);
      motor1.stop();
      motor2.stop();
    }

  // b = rück
      //char text[] = "b";
  if (strcmp(&inDat, text) == 0) {
      motor1.run(255);
      delay(5000);
      motor1.stop();
      motor2.stop();
    }
    
  // c = drehen
      char text[] = "c";
  if (strcmp(&inDat, text) == 0) {
      motor1.run(-255);
      motor2.run(-255);
      delay(5000);
      motor1.stop();
      motor2.stop();
    }
  
}
