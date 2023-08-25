import pyodbc
import subprocess
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs

CommandList = []
cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=192.168.88.228\Storagebase;DATABASE=Storage Force;uid=sa;pwd=BSDGG.in21')
cursor = cnxn.cursor()

def WegFindung(RoboID):
    ID = str(RoboID)
    cursor.execute('SELECT StartPoint,ZielPoint FROM dbo.Roboter WHERE ID =' + ID)
    testnow = cursor.fetchone()
    WegInfo = [row for row in testnow]

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
    
        cursor.execute("UPDATE dbo.Roboter SET ZielPoint = " + Ziel + " WHERE ID = 1")
    
class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed_url = urlparse(self.path)
        query_params = parse_qs(parsed_url.query)
        
        if 'argument' in query_params:
            argument_value = query_params['argument'][0]
            
            print(argument_value)
            
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            response_content = f'Argument received and processed: {argument_value}'
            self.wfile.write(response_content.encode())
        else:
            self.send_response(400)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'Missing argument')

def run_server(server_class=HTTPServer, handler_class=RequestHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Starting server on port {port}")
    httpd.serve_forever()

if __name__ == '__main__':
    run_server()
    p1 = subprocess.Popen('python', 'Robo1.py')
    p2 = subprocess.Popen('python', 'Robo2.py')
    p3 = subprocess.Popen('python', 'Robo3.py')

    while True:
            GetResult = RequestHandler.do_GET()
            if GetResult == "1":
                 WegFindung(1)
            elif GetResult == "2":
                 WegFindung(2)
            elif GetResult == "3":
                 WegFindung(3)
            elif GetResult == "Fehler":
                 p1.terminate()
                 p2.terminate()
                 p3.terminate()
                 while True:
                      print("FEHLER!")
            else:
                 nichts = nichts 
            
           
