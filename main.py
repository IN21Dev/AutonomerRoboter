import pyodbc
import requests
from flask import Flask, request

app = Flask(__name__)
CommandList = []
cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=192.168.88.228\Storagebase;DATABASE=Storage Force;uid=sa;pwd=BSDGG.in21')
cursor = cnxn.cursor()

def WegFindung(RoboID):
    ID = str(RoboID)
    cursor.execute('SELECT StartPoint,ZielPoint FROM dbo.Roboter WHERE ID =' + ID)
    testnow = cursor.fetchone()
    WegInfo = [row for row in testnow]
    print(WegInfo)
    if(WegInfo[0] == WegInfo[1]):
        return
    else:
        cursor.execute("EXEC dbo.usp_Breadth_First " + WegInfo[0] + "," + WegInfo[1])
        QueryResult = cursor.fetchone()
        ListResult = [row for row in QueryResult]
        ZielResult = ListResult[3]
        ZielPfad = ZielResult.split(",")
        Ziel = str(ZielPfad[1])
        NameResult = ListResult[4]
        NameCompare = NameResult.split(",")
        if(NameCompare[0] == (NameCompare[1] - 100)):   
            Erfolg = RoboMove(RoboID,"N")
        elif(NameCompare[1] == (NameCompare[0] -100)):
            Erfolg = RoboMove(RoboID,"S")
        elif(NameCompare[0] < NameCompare[1]):
            Erfolg = RoboMove(RoboID,"O")
        elif(NameCompare[0] > NameCompare[1]):
            Erfolg = RoboMove(RoboID,"W")
        else:
            return
    if(Erfolg == "Ja"):
        cursor.execute("UPDATE dbo.Roboter SET ZielPoint = " + Ziel + " WHERE ID = 1")
    elif(Erfolg == "Nein"):
        raise RuntimeError("Problem mit Roboter!!!")
    
def RoboMove(RoboID,Richtung):
        #Sende Befehl zu Roboter mit Richtung
        if(RoboID == 1):
            RoboAdresse = ""
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
        WegFindung(1)