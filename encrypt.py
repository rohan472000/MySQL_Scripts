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
    cursor.execute("UPDATE rohn2 SET roll=%s WHERE roll=%s", (encrypted_data, sensitive_data))

db.commit()
print("Data encrypted and updated successfully")

# mysql> select * from rohn2;
# +-------+------------------------------------------------------------------------------------------------------+
# | name  | roll                                                                                                 |
# +-------+------------------------------------------------------------------------------------------------------+
# | sohan | gAAAAABkTlvBmIjqYLvgRWr-1ku4K_1ptUgllZZuu8Eiaq00e74JT7_PA-ZXqkhvFB26bAdLiaTAuooYd82I1vmra0G2Pn_BHw== |
# | johan | gAAAAABkTlvBflR2Tr15N-hWIQK_0cdqa7yyjwM1donV4NWkzGLaeewoZKPGkz1DtNRxeS5khBnGI9kMeyIcDFO44mEdUzpiQw== |
# +-------+------------------------------------------------------------------------------------------------------+
# 2 rows in set (0.00 sec)
