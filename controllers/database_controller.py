from abc import ABC, abstractmethod

class Database(ABC):
    # Funzione astratta per creare un database
    @abstractmethod
    def create_database(self):
        pass

    # Funzione astratta per eliminare un database
    @abstractmethod
    def delete_database(self):
        pass

    # Funzione astratta per modificare un database esistente
    @abstractmethod
    def modify_database(self):
        pass

    # Funzione astratta per mostrare i database presenti
    @abstractmethod
    def show_list_database(self):
        pass
