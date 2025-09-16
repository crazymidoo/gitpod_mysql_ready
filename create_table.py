# Questo programma si connette al database MySQL chiamato "mydatabase".
# Utilizza l'host "localhost", l'utente "pythonuser" e la password "password123".
# Dopo aver creato la connessione, viene creato un cursore per eseguire le operazioni nel database.
# La query successiva crea una tabella chiamata "customers", con due colonne: "name" e "address".
# Entrambe le colonne sono di tipo VARCHAR, cioè possono contenere stringhe di testo fino a 255 caratteri.

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="pythonuser",
  password="password123",
  database="mydatabase"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")
