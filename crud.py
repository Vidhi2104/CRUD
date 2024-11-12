import mysql.connector
from mysql.connector import Error

# Establish a connection to the MySQL database
def create_connection():
    try:
        connection = mysql.connector.connect(
            host='localhost',            # Database host (use the correct host)
            user='root',                 # Database user (use the correct username)
            password='VidhI@17',         # Database password (use the correct password)
            database='Curd'   # Database name
        )
        if connection.is_connected():
            print("Connection to MySQL established successfully.")
        return connection
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
        return None
# 1. CREATE Operation: Add a new registrant
def create_registration(first_name, last_name, email, dob, phone=None, gender='Prefer not to say', address=None, city=None, state=None, zip_code=None, country=None):
    try:
        # Establish the connection
        connection = create_connection()
        if connection:
            cursor = connection.cursor()
            
            # SQL query to insert the new registrant
            query = """INSERT INTO Registration 
                        (FirstName, LastName, Email, DateOfBirth, PhoneNumber, Gender, Address, City, State, ZipCode, Country)
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
            
            # Values to be inserted, we use 'None' for optional fields
            values = (first_name, last_name, email, dob, phone, gender, address, city, state, zip_code, country)
            
            # Execute the query and commit the changes
            cursor.execute(query, values)
            connection.commit()
            print(f"Registrant {first_name} {last_name} added successfully!")
    
    except Error as e:
        print(f"Error: {e}")
    
    finally:
        # Close the connection to the database
        if connection and connection.is_connected():
            connection.close()

# Insert Data
create_registration(
    first_name='Vidhi',
    last_name='Mehta',
    email='vidhi@gmail.com',
    dob='2004-10-02',  # Date of Birth in the format 'YYYY-MM-DD'
    phone='997-876-5123',
    gender='Female',
    address='Otiv Apartment Dandiya Bazar',
    city='Vadodara',
    state='Gujarat',
    zip_code='390001',
    country='India'
)
create_registration(
    first_name='Amisha',
    last_name='Tiwari',
    email='Amisha@gmail.com',
    dob='2002-11-19',  # Date of Birth in the format 'YYYY-MM-DD'
    phone='954-984-4567',
    gender='Female',
    address='Sky High tower Dandiya Bazar',
    city='Vadodara',
    state='Gujarat',
    zip_code='390001',
    country='India'
)
create_registration(
    first_name='Mamta',
    last_name='Shah',
    email='mamta@gmail.com',
    dob='1992-07-27',  # Date of Birth in the format 'YYYY-MM-DD'
    phone='912-987-2983',
    gender='Female',
    address='Vijay tower Kandivali west',
    city='Mumbai',
    state='Maharashtra',
    zip_code='400067',
    country='India'
)
create_registration(
    first_name='Kanth',
    last_name='Rathod',
    email='Kanth@gmail.com',
    dob='1999-12-09',  # Date of Birth in the format 'YYYY-MM-DD'
    phone='982-886-4358',
    gender='Male',
    address='Shubhas Tower Kandivali East',
    city='Mumbai',
    state='Maharashtra',
    zip_code='400101',
    country='India'
)
create_registration(
    first_name='Vansh',
    last_name='Dubey',
    email='Vansh@gmail.com',
    dob='2005-12-19',  # Date of Birth in the format 'YYYY-MM-DD'
    phone='977-065-4675',
    gender='Male',
    address='Gods gift tower Boriwali',
    city='Mumbai',
    state='Maharashtra',
    zip_code='400091',
    country='India'
)

# 2. READ Operation: Retrieve a registrant by ID or email
def read_registration(identifier, by='ID'):
    try:
        connection = create_connection()
        if connection:
            cursor = connection.cursor()
            if by == 'ID':
                query = "SELECT * FROM Registration WHERE ID = %s"
            elif by == 'Email':
                query = "SELECT * FROM Registration WHERE Email = %s"
            cursor.execute(query, (identifier,))
            result = cursor.fetchone()
            if result:
                print("Registrant Details:", result)
            else:
                print("No record found.")
    except Error as e:
        print(f"Error: {e}")
    finally:
        if connection and connection.is_connected():
            connection.close()


# 3. UPDATE Operation: Update registrant's information by ID
def update_registration(id, field, value):
    try:
        connection = create_connection()
        if connection:
            cursor = connection.cursor()
            query = f"UPDATE Registration SET {field} = %s WHERE ID = %s"
            cursor.execute(query, (value, FirstName))
            connection.commit()
            print(f"Registrant {id} updated successfully!")
    except Error as e:
        print(f"Error: {e}")
    finally:
        if connection and connection.is_connected():
            connection.close()

# 4. DELETE Operation: Delete a registrant by ID
def delete_registration(id):
    try:
        connection = create_connection()
        if connection:
            cursor = connection.cursor()
            query = "DELETE FROM Registration WHERE ID = %s"
            cursor.execute(query, (id,))
            connection.commit()
            print(f"Registrant {id} deleted successfully!")
    except Error as e:
        print(f"Error: {e}")
    finally:
        if connection and connection.is_connected():
            connection.close()

