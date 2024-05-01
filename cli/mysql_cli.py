from controllers.mysql_controller import MySQLDatabase
from getpass import getpass

def main():
    db = MySQLDatabase()
    while not db.connect():
        print("\nMySQL database")
        print("Connessione al database")
        host = input("Host 'localhost' (default): ")
        port = input("Port '3306' (default): ")
        user = input("User '' (default): ")
        password = getpass("Password '' (default): ")

        if host == "":
            if port == "":
                db = MySQLDatabase(user=user, password=password)
            else:
                db = MySQLDatabase(user=user, password=password, port=port)
        else:
            if port == "":
                db = MySQLDatabase(user=user, password=password, host=host)
            else:
                db = MySQLDatabase(user=user, password=password, host=host, port=port)
        db.connect()

    while True:
        print("\nMySQL database")
        print("Informazioni sulla connessione al database:")
        print(f"Host: {db.host}")
        print(f"Port: {db.port}")
        print(f"User: {db.user}")
        print("Scegliere un'operazione:")
        print("(1) Creare un database")
        print("(2) Eliminare un database")
        print("(3) Torna al menu principale")

        choice = input("Scelta: ")
        match choice:
            case "1":
                db.create_database()
            case "2":
                db.delete_database()
            case "3":
                print("Arrivederci!")
                break
            case _:
                print("Scelta non valida")
