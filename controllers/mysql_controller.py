import mysql.connector
from mysql.connector import Error

from controllers.database_controller import DatabaseController

class __MySQLDatabase(DatabaseController):

    def __init__(self, host='localhost', port=3306, user='', password=''):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.conn = self.connect()
        self.cursor = self.conn.cursor()

    def connect_database(self):
        try:
            conn = mysql.connector.connect(
                host=self.host,
                port=self.port,
                user=self.user,
                password=self.password
            )
            print("Connessione al database riuscita")
            return True
        except Error as e:
            print("Connessione al database fallita")
            print(e)
            return False

    def disconnect_database(self):
        try:
            self.conn.close()
            print("Disconnessione dal database riuscita")
            self.connected = False
            return True
        except Error as e:
            print("Disconnessione al database fallita")
            print(e)
            return False

    def create_database(self):
        try:
            db_name = input("Inserire il nome del database: ")
            self.cursor(f"CREATE DATABASE {db_name}")
            print("Database creato con successo")
        except Error as e:
            print("Creazione del database fallita")
            print(e)
    
    def delete_database(self):
        try:
            self.show_list_database()
            db_name = input("Inserire il nome del database da eliminare: ")
            self.cursor.execute(f"DROP DATABASE {db_name}")
            print("Database eliminato con successo")
        except Error as e:
            print("Eliminazione del database fallita")
            print(e)
    
    def modify_database(self):
        try:
            self.show_list_database()
            db_name = input("Inserire il nome del database da modificare: ")
            self.cursor.execute(f"USE DATABASE {db_name}")
        except Error as e:
            print("Modifica del database fallita")
            print(e)

    def show_list_database(self):
        self.cursor.execute("SHOW DATABASES")
        databases = self.cursor.fetchall()
        print("Database presenti:")
        for db in databases:
            print(db[0])
