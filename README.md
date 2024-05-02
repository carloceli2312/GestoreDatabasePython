# Programma di Gestione dei Database

Questo programma consente di gestire i database. È possibile connettersi a un database e eseguire varie operazioni.

## Requisiti

Per eseguire il programma, è necessario avere installato Python 3.10 o versioni successive, e i moduli nel file requirements.txt.

Per installare i moduli necessari, esegui il seguente comando:

```bash
pip install -r requirements.txt
```

## Come eseguire il programma

Per eseguire il programma, avvia il file `main.py` nel tuo terminale. Verrà visualizzato un menu con le seguenti opzioni:

1. Connettersi a un database
2. Uscire dal programma

Inserisci il numero corrispondente alla tua scelta e premi Invio.

### Connettersi a un database

Se scegli di connetterti a un database, verrà visualizzato un menu con le seguenti opzioni:

1. SQLite
2. MySQL
3. Esci

Inserisci il numero corrispondente alla tua scelta e premi Invio.

#### SQLite

Se scegli di connetterti a un database SQLite, verrà visualizzato un menu con le seguenti opzioni:

1. Crea un nuovo database
2. Elimina un database
3. Modifica un database
4. Visualizza i database presenti
5. Indietro

I database SQLite su cui si lavorerà saranno tutti salvati nella cartella 'sqlite_db'.

#### MySQL

Se scegli di connetterti a un database MySQL, all'avvio di questa modalità verrà visualizzato un menu con le seguenti opzioni per effettuare la connessione:

1. Inserire l'host, 'localhost' (default): inserisci l'host del database MySQL.
2. Inserire la porta, '3306' (default): inserisci la porta del database MySQL.
3. Inserire l'username, 'root' (default): inserisci il nome utente del database MySQL.
4. Inserire la password, 'password' (default): inserisci la password del database MySQL.

Se la connessione è avvenuta con successo, verrà visualizzato un menu con le seguenti opzioni:

1. Crea un nuovo database
2. Elimina un database
3. Modifica un database
4. Visualizza i database presenti
5. Chiudi la connessione

## Licenza

Questo software è rilasciato sotto la licenza MIT. Per ulteriori dettagli, consulta il file [LICENSE](LICENSE).

## Autore

Carlo Giuseppe Celi
