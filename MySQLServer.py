import mysql.connector


def create_database():
    
    connection = None
    cursor = None

    try:
        # Connect to MySQL server (adjust host, user, password if needed)

        connection = mysql.connector.connect(
            host="localhost",
            user="root",  # username
            password="Mcddlove/92*",  # password
            port=3306,  # Default MySQL port
        )

        if connection.is_connected():
            cursor = connection.cursor()

            # Create database if it doesn't exist
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")

            print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as e:
        print(f"Error connecting to MySQL database: {e}")

    finally:
        # Close cursor and connection
        if cursor:
            cursor.close()
        if connection and connection.is_connected():
            connection.close()


if __name__ == "__main__":
    create_database()