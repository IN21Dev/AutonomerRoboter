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

while True:
        