import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'Mothergracia'
)

cursorObject = dataBase.cursor()
cursorObject.execute("CREATE DATABASE idrice1")
print("we are done")