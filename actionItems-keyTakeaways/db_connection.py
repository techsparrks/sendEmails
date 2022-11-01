import mysql.connector
from mysql.connector import Error
from load_credentials import load_sparrksapp_db_credentials as load

def connect():
    connection = None
    try:
        connection = mysql.connector.connect(
            host = load('host'),
            user = load('user'),
            password = load('password'),
            database = load('database')
        )
        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")
    return connection

def close(connection):
    if connection.is_connected():
        cursor = connection.cursor()
        cursor.close()
        connection.close()
        print("MySQL connection is closed")
