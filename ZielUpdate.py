import pyodbc

while True:

    CommandList = []
    cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=192.168.88.223\Storagebase;DATABASE=Storage Force;uid=sa;pwd=BSDGG.in21')
    cursor = cnxn.cursor()

    RoboID = input("Gebe Roboter ID ein: ")
    RoboZiel = input("Gebe Roboter Ziel ein: ")

    cursor.execute("UPDATE dbo.Roboter SET ZielPoint = " + RoboZiel + " WHERE ID =" + RoboID)
    cursor.commit()