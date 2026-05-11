<<<<<<< HEAD
import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="trolley.proxy.rlwy.net",
        user="root",
        password="NdybOrqojHEAObBlFJAKdTSvPAJeOumM",
        database="railway"
        port = 29453
    )
=======
import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="client_query_db"
    )
>>>>>>> 4811b26a3e09bb229017e272c19693076682b618
