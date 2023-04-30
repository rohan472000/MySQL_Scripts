import subprocess
import datetime
import os

# Set the database connection details
db_host = "localhost"
db_user = "root"
db_password = "rohan"
db_name = "sakila"

# Set the backup directory
backup_dir = "backup-directory"

# Get the current date and time
now = datetime.datetime.now()
timestamp = now.strftime("%Y-%m-%d_%H-%M-%S")

# Set the backup file name
backup_file = f"{db_name}_{timestamp}.sql"

# Create the backup command
backup_command = f"mysqldump -h {db_host} -u {db_user} -p{db_password} {db_name} > {backup_dir}/{backup_file}"

# Execute the backup command
try:
    subprocess.check_call(backup_command, shell=True)
    print("Backup created successfully!")
except subprocess.CalledProcessError as e:
    print(f"Error creating backup: {e}")

# List the backup files in the backup directory
backup_files = os.listdir(backup_dir)
backup_files.sort(reverse=True)

# Keep the 5 most recent backup files
if len(backup_files) > 5:
    for file in backup_files[5:]:
        os.remove(os.path.join(backup_dir, file))
