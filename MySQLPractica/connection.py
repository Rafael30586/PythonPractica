import mysql.connector

database = mysql.connector.connect(
    host="localhost",
    user="root",
    password="rafael",
    database="empleados"
)

cursorObject = database.cursor()
query = "SELECT nombre, apellido1 FROM empleado"
cursorObject.execute(query)

myResult = cursorObject.fetchall()

for x in myResult:
    print(x)

database.close()