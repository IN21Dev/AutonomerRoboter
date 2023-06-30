import pyodbc
import requests
from flask import Flask, request

app = Flask(__name__)

def RoboMove(RoboID,Richtung):
        #Sende Befehl zu Roboter mit Richtung
        if(RoboID == 1):
            RoboAdresse = "192.168.88.232:85/endpoint"
        elif(RoboID == 2):
            RoboAdresse = ""
        elif(RoboID == 3):
            RoboAdresse = ""
        else:  
            return
        response = requests.post(RoboAdresse, data=Richtung)  
        #Warte/Bearbeite Antwort
        if response.status_code == 200:
            while True:
                @app.route('/endpoint', methods=['POST'])
                def handle_post_request():
                    data = request.form
                    return data
        else:
            print("POST request failed!")
            return "Nein"
        
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
    while True:
        stuff = input("Gebe Richtung ein (1,2,3,4)")
        RoboMove(input)