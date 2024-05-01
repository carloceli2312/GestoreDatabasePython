import cli.database_cli as database_cli

def main():
    while True:
        print("\nBenvenuto nel programma di gestione dei database")
        print("Scegliere una delle seguenti opzioni:")
        print("(1) Connettersi a un database")
        print("(2) Uscire dal programma")

        choice = input("Scelta: ")
        match choice:
            case "1":
                database_cli.main()
            case "2":
                print("Arrivederci!")
                break
            case _:
                print("Scelta non valida")
