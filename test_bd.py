import MySQLdb

try:
    conn = MySQLdb.connect(
        host="localhost",
        user="dev",
        password="password",
        database="makkarriz"
    )
    print("Connexion réussie à la base de données !")
    conn.close()
except Exception as e:
    print(f"Erreur de connexion : {e}")
