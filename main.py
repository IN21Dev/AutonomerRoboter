import pyodbc

server = "localhost\sqlexpress"
database = "RoboTest"
username = "RoboAdmin"
password = "TestAdmin"

cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=localhost\sqlexpress;DATABASE=RoboTest;Trusted_Connection=yes;')
cursor = cnxn.cursor()

file = open("C:\Service\Test.txt")
with open("C:\Service\Test.txt") as f:
    mylist = f.read().splitlines() 
    result = [item.split(",")for item in mylist]

for x in result:
    command1 ="'" + x[0] + "'"
    command2 ="'" + x[1] + "'"
    command3 ="'" + x[2] + "'"
    command4 ="'" + x[3] + "'"
    cursor.execute("INSERT INTO [dbo].[RoboPath] VALUES (" + command1 + "," + command2  + "," + command3  + "," + command4 + ")")
cnxn.commit()
cnxn.close()