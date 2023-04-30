# before running this scripts :- 
# mysql> select * from rohn2;
# +-------+------+
# | name  | roll |
# +-------+------+
# | sohan |  221 |
# | johan |  231 |
# +-------+------+
# 2 rows in set (0.00 sec)

from cryptography.fernet import Fernet
import mysql.connector

# Connect to MySQL database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="rohan",
    database="mohn"
)

# Generate encryption key
key = Fernet.generate_key()

# Create Fernet object with the key
f = Fernet(key)

# Query sensitive data from MySQL database
cursor = db.cursor()
cursor.execute("SELECT roll FROM rohn2")
result = cursor.fetchall()

# Encrypt sensitive data and update MySQL database
for row in result:
    global encrypted_data
    sensitive_data = str(row[0])
    encrypted_data = f.encrypt(sensitive_data.encode())
    cursor.execute("UPDATE rohn2 SET roll=%s WHERE roll=%s", 
                   (encrypted_data, sensitive_data))

db.commit()
print("Data encrypted and updated successfully")

# after running above scripts :-
# mysql> select * from rohn2;
# +-------+-------------------+
# | name  | roll              |
# +-------+-------------------+
# | sohan | gAAAAABkTl==      |
# | johan | gKPGkz1DdUzpiQw== |
# +-------+-------------------+
# 2 rows in set (0.00 sec)
