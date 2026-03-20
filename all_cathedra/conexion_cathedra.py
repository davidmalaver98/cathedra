import mysql.connector
conexion = mysql.connector.connect(
 host="localhost",
 user="root",
 password="root",
 database="cathedra",
 port="3306"
)
print(conexion)
