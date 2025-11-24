import sys
import mysql.connector
from mysql.connector import errorcode

# ---------------------------------------------------------
# DATABASE CONNECTION SETUP
# ---------------------------------------------------------
def get_db_connection():
    """
    Establishes and returns a connection to the database.
    Update the user, password, and database fields below.
    """
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",      # Your MySQL username (usually root)
            password="7501",  # <--- PUT YOUR MYSQL PASSWORD HERE
            database="cs122a_project"  # The name of your database
        )
        return connection
    except mysql.connector.Error as err:
        print(f"Error connecting to DB: {err}")
        return None

# ---------------------------------------------------------
# FUNCTION 1: IMPORT DATA
# ---------------------------------------------------------
def import_data(folder_name):
    """
    Drops existing tables, creates new ones (DDL), and imports .csv data.
    """
    conn = get_db_connection()
    if conn is None:
        return

    cursor = conn.cursor()
    print(f"Importing data from folder: {folder_name}...")

    try:
        # TODO: 1. Read your DDL file (from HW2) and execute commands to create tables
        # Example: cursor.execute("CREATE TABLE ...")
        
        # TODO: 2. Iterate through CSV files in 'folder_name' and INSERT data
        # Example: using LOAD DATA LOCAL INFILE or simple INSERT loops
        
        conn.commit()
        print("Success") # Requirement: Print "Success" or "Fail" [cite: 81]
    except Exception as e:
        print("Fail")
        print(e)
    finally:
        cursor.close()
        conn.close()

# ---------------------------------------------------------
# MAIN EXECUTION LOOP
# ---------------------------------------------------------
if __name__ == "__main__":
    # Check if a function name is provided
    if len(sys.argv) < 2:
        print("Usage: python3 project.py <function_name> [params]")
        sys.exit(1)

    function_name = sys.argv[1]
    
    # Dispatcher: Calls the correct function based on the command line argument
    if function_name == "import":
        # Requirement: python3 project.py import [folderName] [cite: 93]
        if len(sys.argv) != 3:
            print("Usage: python3 project.py import <folder_name>")
        else:
            import_data(sys.argv[2])
            
    # TODO: Add elif blocks for other functions (insertAgentClient, etc.) here
    
    else:
        print(f"Unknown function: {function_name}")