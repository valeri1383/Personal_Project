import mysql.connector


# Establish a connection to the MySQL database
conn = mysql.connector.connect(
    host='YOUR_HOST',
    user='YOUR_USERNAME',
    password='YOUR_PASSWORD',
    database='YOUR_DATABASE'
)

def register_user(username, password):
    try:
        # Create a cursor object to execute SQL statements
        cursor = conn.cursor()

        # Execute the SQL INSERT statement
        sql = "INSERT INTO users (username, password) VALUES (%s, %s)"
        values = (username, password)
        cursor.execute(sql, values)

        # Commit the changes
        conn.commit()

        print("User registered successfully!")
    except mysql.connector.Error as e:
        print("Error registering user:", str(e))
    finally:
        # Close the cursor
        cursor.close()

register_user("john_doe", "password123")



def check_user(username):
    try:
        # Create a cursor object to execute SQL statements
        cursor = conn.cursor()

        # Execute the SQL SELECT statement
        sql = "SELECT * FROM users WHERE username = %s"
        values = (username,)
        cursor.execute(sql, values)

        # Fetch the result
        result = cursor.fetchone()

        if result:
            print("User exists")
        else:
            print("User does not exist")
    except mysql.connector.Error as e:
        print("Error checking user:", str(e))
    finally:
        # Close the cursor
        cursor.close()


check_user("john_doe")
