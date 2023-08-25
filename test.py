import pyodbc
import requests
import urllib3
import time
import http.server
import socketserver


resp = urllib3.request("GET", "192.168.88.232:8000/?argument=7")