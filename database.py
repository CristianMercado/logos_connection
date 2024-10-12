import mysql.connector

database = mysql.connector.connect(
    host= 'localhost',
    user= 'root',
    password= 'Proyecto1234Modular',
    database= 'logos_connection_db',
    port= 3306,
)