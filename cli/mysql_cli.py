from controllers.database_controller import DatabaseController
from getpass import getpass

def main():
    temp = False
    while not temp:
        print("\nMySQL database")
        print("Connessione al database")
        host = input("Inserire l'host, 'localhost' (default): ")
        port = input("Inserire la porta, '3306' (default): ")
        user = input("Inserire l'username, '' (default): ")
        password = getpass("Inserire la password, '' (default): ")
        if host == '':
            host = 'localhost'
        if port == '':
            port = 3306
        db = DatabaseController()
        temp = db.connect_database()

    while True:
        print("\nMySQL database")
        print("Informazioni sulla connessione al database:")
        print(f"Host: {host}")
        print(f"Port: {port}")
        print(f"User: {user}")
        print("Scegliere un'operazione:")
        print("(1) Crea un nuovo database")
        print("(2) Elimina un database")
        print("(3) Modifica un database")
        print("(4) Mostra i database presenti")
        print("(5) Chiudi la connessione")

        choice = input("Scelta: ")
        match choice:
            case "1":
                db.create_database()
            case "2":
                db.delete_database()
            case "3":
                db.modify_database()
            case "4":
                db.show_list_database()
            case "5":
                print("Chiusura connessione al database")
                db.disconnect_database()
                break
            case _:
                print("Scelta non valida")
