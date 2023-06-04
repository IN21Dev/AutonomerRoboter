import pyodbc

server = "localhost\sqlexpress"
database = "RoboTest"
username = "SA"
password = "TestAdmin"

cnxn = pyodbc.connect('DRIVER={ODBC Driver 18 for SQL Server};SERVER='+server+';DATABASE='+database+';ENCRYPT=yes;UID='+username+';PWD='+ password)
cursor = cnxn.cursor()

