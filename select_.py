# Questo programma si connette al database "mydatabase" su MySQL, utilizzando l'utente "pythonuser" e la password "password123".
# Dopo aver stabilito la connessione, viene creato un cursore per eseguire le operazioni nel database.
# La query SQL "SELECT * FROM customers" viene eseguita per recuperare tutte le righe dalla tabella "customers".
# Il risultato della query viene memorizzato nella variabile `myresult` utilizzando il metodo `fetchall()`, 
# che recupera tutte le righe trovate nella tabella.
# Il ciclo `for` scorre tutte le righe di `myresult` e le stampa una per una.

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="pythonuser",
  password="password123",
  database="mydatabase"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM customers")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
