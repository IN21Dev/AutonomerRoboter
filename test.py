import pyodbc
import requests
import urllib3
import time
import http.server
import socketserver


CommandList = []
cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=192.168.88.223\Storagebase;DATABASE=Storage Force;uid=sa;pwd=BSDGG.in21')
cursor = cnxn.cursor()

ID = str(1)
cursor.execute('SELECT StartPoint,ZielPoint FROM dbo.Roboter WHERE ID =' + ID)
testnow = cursor.fetchone()
WegInfo = [row for row in testnow]
StringForm = [str(x) for x in WegInfo]

cursor.execute("EXEC dbo.usp_Breadth_First " + StringForm[0] + "," + StringForm[1])
QueryResult = cursor.fetchone()
ListResult = [row for row in QueryResult]
ZielResult = ListResult[3]        
ZielPfad = ZielResult.split(",")
print(ZielPfad)