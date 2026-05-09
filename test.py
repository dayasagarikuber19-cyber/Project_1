import sys
print("Step 1: Starting", flush=True)

import mysql.connector
print("Step 2: Module imported", flush=True)

try:
    conn = mysql.connector.connect(
        host="trolley.proxy.rlwy.net",
        user="root",
        password="NdybOrqojHEAObBlFJAKdTSvPAJeOumM",
        database="railway",
        port=29453
    )
    print("Step 3: Connected!", flush=True)
    cursor = conn.cursor()
    cursor.execute("SHOW TABLES")
    tables = cursor.fetchall()
    print("Step 4: Tables:", tables, flush=True)
    conn.close()
except Exception as e:
    print("Error:", e, flush=True)

print("Step 5: Done!", flush=True)