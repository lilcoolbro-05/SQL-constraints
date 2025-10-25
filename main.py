import sqlite3 
database = "MYDATABASE.sqlite"
con=sqlite3.connect(database)
print("Database connected successfully")

con.execute(''' 
CREATE TABLE IF NOT EXISTS USERS
(ID INTEGER PRIMARY KEY,
NAME TEXT NOT NULL,
AGE INT NOT NULL);
''')
print("Table created successfully")

con.execute('''
INSERT INTO USERS (ID,NAME,AGE)
VALUES (1,'Gabriel',17);
''')
import pandas as pd



