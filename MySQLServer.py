import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Connect to MySQL server
        connection = mysql.connector.connect(
            host="localhost",  # Change if needed
            user="your_username",  # Replace with your MySQL username
            password="your_password"  # Replace with your MySQL password
        )

        if connection.is_connected():
            cursor = connection.cursor()
            try:
                # Create database if it doesn't exist
                cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store;")
                print("Database 'alx_book_store' created successfully!")
            except mysql.connector.Error as e:
                print(f"Error creating database: {e}")
            finally:
                cursor.close()

    except mysql.connector.Error as e:
        print(f"Error connecting to MySQL server: {e}")

    finally:
        if connection.is_connected():
            connection.close()
            print("MySQL connection is closed.")

if __name__ == "__main__":
    create_database()
