#include <ArduinoRobot.h>

void setup(){
  Robot.begin();
  Serial.begin(9600);
}

class Movement {
	public:
	int Feldzeit=1000 //Hier ist die Zeit in ms einzusetzen, in der der Roboter bei Vollgeschwindigkeit ein Feld zurücklegt
	int Drehzeit=1000 //Hier ist die Zeit in ms einzusetezen, in der der Roboter sich bei Vollgeschwindigkeit um 90° dreht

//Fahre n Felder vorwärts:
	void drive(n) {
		Robot.motorsWrite(255,255);
		delay(n*Feldzeit);
		Robot.motorsWrite(0,0);
}

//Fahre n Felder rückwärts:
	void driveBack(n) {
		Robot.motorsWrite(-255,-255);
		delay(n*Feldzeit);
		Robot.motorsWrite(0,0);
}

//Drehe dich um 90° nach rechts:
	void turnRight() {
		Robot.motorsWrite(255,-255);
		delay(Drehzeit);
		Robot.motorsWrite(0,0);
}

//Drehe dich um 90° nach links:
	void turnLeft() {
		Robot.motorsWrite(-255,255);
		delay(Drehzeit);
		Robot.motorsWrite(0,0);
}
};