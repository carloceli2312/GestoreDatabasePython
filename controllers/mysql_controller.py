import mysql.connector
from mysql.connector import Error

from controllers.database_controller import Database

class MySQLDatabase(Database):

    def __init__(self, host='localhost', port=3306, user='', password=''):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.conn = None
        self.cursor = None

    def connect(self):
        try:
            with mysql.connector.connect(
                host=self.host,
                port=self.port,
                user=self.user,
                password=self.password
            ) as conn:
                self.conn = conn
                self.cursor = self.conn.cursor()
                print("Connessione al database riuscita")
                return True
        except Error as e:
            print("Connessione al database fallita")
            print(e)
            return False

    def create_database(self):
        try:
            db_name = input("Inserire il nome del database: ")
            self.cursor.execute(f"CREATE DATABASE {db_name}")
            print("Database creato con successo")
        except Error as e:
            print("Creazione del database fallita")
            print(e)
    
    def delete_database(self):
        pass
    
    def modify_database(self):
        pass

    def show_list_database(self):
        pass
