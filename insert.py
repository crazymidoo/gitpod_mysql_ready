# Questo programma si connette al database "mydatabase" su MySQL, utilizzando l'utente "pythonuser" e la password "password123".
# Dopo aver stabilito la connessione, viene creato un cursore per eseguire le operazioni nel database.
# La variabile `sql` contiene la query SQL per inserire un nuovo record nella tabella "customers", 
# dove si inseriscono i valori per "name" e "address".
# La variabile `val` contiene i dati da inserire (in questo caso, il nome "John" e l'indirizzo "Highway 21").
# La funzione `execute` esegue la query con i valori passati.
# Poi, `mydb.commit()` salva le modifiche nel database.
# Infine, viene stampato il numero di record inseriti, che in questo caso sarà 1.

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="pythonuser",
  password="password123",
  database="mydatabase"
)

mycursor = mydb.cursor()

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("John", "Highway 21")
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")
