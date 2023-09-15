import pyodbc
import urllib3
import time
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed_url = urlparse(self.path)
        query_params = parse_qs(parsed_url.query)
        
        if 'argument' in query_params:
            argument_value = query_params['argument'][0]
            
            print("Argument:", argument_value)
            
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            return argument_value
        else:
            self.send_response(400)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'Missing argument')
            return "Nein"

def run_server(server_class=HTTPServer, handler_class=RequestHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Starting server on port {port}")
    httpd.serve_forever()

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
            Erfolg = RoboMove(RoboID,"0")
        elif(NameCompare[1] == (NameCompare[0] -100)):
            Erfolg = RoboMove(RoboID,"1")
        elif(NameCompare[0] < NameCompare[1]):
            Erfolg = RoboMoveRight(RoboID,Ziel)
        elif(NameCompare[0] > NameCompare[1]):
            Erfolg = RoboMoveLeft(RoboID,Ziel)
        else:
            return
    
def RoboMove(RoboID,Richtung):
        #Sende Befehl zu Roboter mit Richtung
        if(RoboID == 1):
            RoboAdresse = "192.168.88.232:85/TEST?" + Richtung
        elif(RoboID == 2):
            RoboAdresse = ""
        elif(RoboID == 3):
            RoboAdresse = ""
        else:  
            return
        resp = urllib3.request("GET", RoboAdresse)
        #Warte/Bearbeite Antwort
        if resp.status == 200:
                response = ""
                while not response:
                    response = RequestHandler.do_GET()
                return response

    
def RoboMoveRight(RoboID,Ziel):
        #Sende Befehl zu Roboter mit Richtung
        if(RoboID == 1):
            RoboAdresse = "192.168.88.232:85/?argument=2"
        resp = urllib3.request("GET", RoboAdresse)
        #Warte/Bearbeite Antwort
        time.sleep(5.0)
        RoboAdresse = "192.168.88.232:85/?argument=0"
        resp = urllib3.request("GET", RoboAdresse)
        if resp.status == 200:
            cursor.execute("UPDATE dbo.Roboter SET ZielPoint = " + Ziel + " WHERE ID = 1")
        else:
            print("GET Request Failed!")
        RoboAdresse = "192.168.88.232:85/?argument=3"
        time.sleep(5.0)
        resp = urllib3.request("GET", RoboAdresse)
        if resp.status == 200:
            return
        else:
            print("GET Request Failed!")
            return "Nein"
        
def RoboMoveLeft(RoboID,Ziel):
        #Sende Befehl zu Roboter mit Richtung
        if(RoboID == 1):
            RoboAdresse = "192.168.88.232:85/?argument=3"
        resp = urllib3.request("GET", RoboAdresse)
        #Warte/Bearbeite Antwort
        time.sleep(5.0)
        RoboAdresse = "192.168.88.232:85/?argument=0"
        resp = urllib3.request("GET", RoboAdresse)
        if resp.status == 200:
            cursor.execute("UPDATE dbo.Roboter SET ZielPoint = " + Ziel + " WHERE ID = 1")
        else:
            print("GET Request Failed!")
        RoboAdresse = "192.168.88.232:85/?argument=2"
        time.sleep(5.0)
        resp = urllib3.request("GET", RoboAdresse)
        if resp.status == 200:
            return
        else:
            print("GET Request Failed!")
            return "Nein"
        
if __name__ == '__main__':
    while True:
        WegFindung(3)