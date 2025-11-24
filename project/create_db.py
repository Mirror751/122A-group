import mysql.connector

# Connect to MySQL Server (without specifying a database yet)
try:
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="7501"  # <--- PUT YOUR MYSQL PASSWORD HERE
    )
    
    cursor = db.cursor()
    
    # Execute the command to create the database
    cursor.execute("CREATE DATABASE cs122a_project")
    
    print("Success! Database 'cs122a_project' created.")
    
except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    if 'db' in locals() and db.is_connected():
        cursor.close()
        db.close()