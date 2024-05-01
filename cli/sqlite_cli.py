from controllers.sqlite_controller import SQLiteDatabase

def main():
    db = SQLiteDatabase()

    while True:
        print("\nSQLite database")
        print("Scegli una delle seguenti opzioni:")
        print("(1) Crea un nuovo database")
        print("(2) Elimina un database")
        print("(3) Modifica un database")
        print("(4) Visualizza i database presenti")
        print("(5) Indietro")

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
                print("Arrivederci!")
                break
            case _:
                print("Scelta non valida")
