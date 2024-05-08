import sqlite3 as sql
import os

from controllers.database_controller import DatabaseController

class __SQLiteDatabase(DatabaseController):
    def __init__(self):
        self.conn = None
        self.cursor = None

    def connect_database(self):
        try:
            db_name = input("\nInserire il nome del database: ")
            self.conn = sql.connect("sqlite_db/" + db_name + '.db')
            self.cursor = self.conn.cursor()
            print("Connessione al database riuscita")
            return True
        except sql.DatabaseError as e:
            print("Connessione al database fallita")
            print(e)
            return False
    
    def disconnect_database(self):
        try:
            self.conn.close()
            print("Disconnessione dal database riuscita")
        except sql.DatabaseError as e:
            print("Disconnessione dal database fallita")
            print(e)

    def create_database(self):
        try:
            self.connect_database()
            self.cursor = self.conn.cursor()
            while True:
                query = input("Inserire la query da eseguire: ")
                self.cursor.execute(query)
                print("Query eseguita con successo")
            print("Database creato con successo")
        except sql.DatabaseError as e:
            print("Creazione del database fallita")
            print(e)
    
    def delete_database(self):
        try:
            self.show_list_database()
            db_name = input("\nInserire il nome del database da eliminare: ")
            self.conn = sql.connect("sqlite_db/" + db_name + '.db')
            self.cursor = self.conn.cursor()
            self.cursor.execute("DROP DATABASE " + db_name)
            print("Database eliminato con successo")
        except sql.DatabaseError as e:
            print("Eliminazione del database fallita")
            print(e)

    def modify_database(self):
        try:
            db_name = input("Inserire il nome del database con cui interagire: ")
            self.conn = sql.connect("sqlite_db/" + db_name + '.db')
            self.cursor = self.conn.cursor()
            while True:
                query = input("Inserire la query da eseguire: ")
                self.cursor.execute(query)
                print("Query eseguita con successo")
        except sql.DatabaseError as e:
            print("Errore durante l'esecuzione della query")
            print(e)

    def show_list_database(self):
        try:
            db_files = [file for file in os.listdir("sqlite_db") if file.endswith(".db")]
            print(f"Number of Databases: {len(db_files)}")
            print("List of Databases:")
            for file in db_files:
                print(file)
        except FileNotFoundError:
            print("Directory 'sqlite_db' not found")
        except Exception as e:
            print("Error occurred while listing databases")
            print(e)
