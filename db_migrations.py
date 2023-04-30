import mysql.connector

# Define connection parameters for the source and destination databases
source_config = {
    'user': 'root',
    'password': 'rohan',
    'host': 'localhost',
    'database': 'mohn'
}

dest_config = {
    'user': 'root',
    'password': 'rohan',
    'host': 'localhost',
    'database': 'rohn'
}

# Establish connections to the source and destination databases
source_conn = mysql.connector.connect(**source_config)
dest_conn = mysql.connector.connect(**dest_config)

# Use SQL commands to extract data from the source database
source_cursor = source_conn.cursor()
source_cursor.execute('SELECT * FROM rohn2')
data = source_cursor.fetchall()

# Use SQL commands to insert the data into the destination database
dest_cursor = dest_conn.cursor()
dest_cursor.executemany('INSERT INTO rohn1 VALUES (%s, %s)', data)
dest_conn.commit()

# Close the connections to the databases
source_cursor.close()
source_conn.close()
dest_cursor.close()
dest_conn.close()
