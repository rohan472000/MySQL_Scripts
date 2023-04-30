# This script uses the psutil library to monitor the CPU and memory usage of the
# system and the mysql.connector library to connect to the MySQL database. It also
# defines two functions: get_system_stats() to get the CPU and memory usage, and
# get_slow_queries() to get a list of slow queries (queries that take more than
# 10 seconds to execute).

# The script then runs a loop for one hour, checking the system stats and slow
# queries every 10 seconds. If any slow queries are found, they are printed to the console.
# After the loop is finished, the database connection is closed.

# You can modify this script to add more performance monitoring tasks,
# such as monitoring disk usage, identifying frequently executed queries,
# and optimizing database indexes.#

import mysql.connector
import psutil
import time

# MySQL database configuration
config = {
    'user': 'root',
    'password': 'rohan',
    'host': 'localhost',
    'database': 'sakila'
}

# Connect to the database
cnx = mysql.connector.connect(**config)
cursor = cnx.cursor()


# Define function to get CPU and memory usage
def get_system_stats():
    cpu_percent = psutil.cpu_percent()
    mem_percent = psutil.virtual_memory().percent
    return (cpu_percent, mem_percent)


# Define function to get slow queries
def get_slow_queries():
    cursor.execute("SELECT * FROM INFORMATION_SCHEMA.PROCESSLIST WHERE TIME > 10")
    return cursor.fetchall()


# Monitor the database for 30 seconds
start_time = time.time()
while time.time() - start_time < 30:
    # Get system stats
    cpu_percent, mem_percent = get_system_stats()
    print(f"CPU usage: {cpu_percent}%, Memory usage: {mem_percent}%")

    # Get slow queries
    slow_queries = get_slow_queries()
    if slow_queries:
        print("Slow queries:")
        for query in slow_queries:
            print(query)

    time.sleep(10)  # Wait for 10 seconds before checking again

# Close the database connection
cursor.close()
cnx.close()
