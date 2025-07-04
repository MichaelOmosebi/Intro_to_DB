import mysql.connector

def create_database():
    mycursor = None
    connection = None
    """This script connects to a MySQL server and creates a database named 'alx_book_store'.
    It will create the database only if it does not already exist."""
    print("Connecting to MySQL server to create 'alx_book_store' database...")
    try:
        # Connect to MySQL server
        connection = mysql.connector.connect(
            host='localhost',
            user='your_username',  # replace with your MySQL username
            password='your_password'  # replace with your MySQL password
        )
        
        mycursor = connection.cursor()
        
        # Create database if it does not exist
        mycursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")
        
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        if mycursor:
            mycursor.close()
        if connection:
            connection.close()

if __name__ == "__main__":
    create_database()
