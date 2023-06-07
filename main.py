import pyodbc

server = "localhost\sqlexpress"
database = "RoboTest"
username = "RoboAdmin"
password = "TestAdmin"
Command = []

cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=localhost\sqlexpress;DATABASE=RoboTest;Trusted_Connection=yes;')
cursor = cnxn.cursor()

cursor.execute("select username, password from users")
row = cursor.fetchall()
if row:
    print(row)


file = open("C:\Service\Test.txt")
for line in file:
   CommandList = line.split(",")
   [Command.append(x) for x in CommandList]

print(Command)

            