from abc import ABC, abstractmethod

class DatabaseController(ABC):
    # Funzione per connettersi ad un database
    @abstractmethod
    def connect_database(self) -> bool:
        pass

    # Funzione per disconnettersi da un database
    @abstractmethod
    def disconnect_database(self) -> bool:
        pass

    # Funzione astratta per creare un database
    @abstractmethod
    def create_database(self) -> object:
        pass

    # Funzione astratta per eliminare un database
    @abstractmethod
    def delete_database(self) -> None:
        pass

    # Funzione astratta per modificare un database esistente
    @abstractmethod
    def modify_database(self) -> object:
        pass

    # Funzione astratta per mostrare i database presenti
    @abstractmethod
    def show_list_database(self) -> list[object]:
        pass
