import cli.sqlite_cli as sqlite_cli
import cli.mysql_cli as mysql_cli

def main():
    while True:
        print("\nConnessione al database")
        print("Scegliere uno tra i seguenti database:")
        print("(1) SQLite")
        print("(2) MySQL")
        print("(3) Esci")

        choice = input("Scelta: ")
        match choice:
            case "1":
                sqlite_cli.main()
            case "2":
                mysql_cli.main()
            case "3":
                print("Arrivederci!")
                break
            case _:
                print("Scelta non valida")
