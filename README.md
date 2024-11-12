# CRUD
This repository contains a simple CRUD (Create, Read, Update, Delete) application that manages user registrations. The application uses an SQL database to store and retrieve registration data, with fields such as FirstName, LastName, Email, DateOfBirth, PhoneNumber, Gender, Address, City, State, ZipCode, Country

Features
Create a new user registration.
Read/display all user registrations or a specific registration by ID.
Update user information.
Delete user registrations.
Technologies Used
Backend: Python 
Database: MySQL 

Prerequisites
Python (version 3.x recommended)
SQL Database MySQL 
Git for cloning the repository

Setup Instructions

1. Clone the Repository
bash
git clone https://github.com/Vidhi2104/CRUD.git
cd registration-crud-app

2. Set up the Database
Create a new database in your SQL server (MySQL or PostgreSQL).
Use the following SQL code to create the Registration table:
sql
CREATE TABLE Registration (
    ID INT PRIMARY KEY AUTO_INCREMENT PRIMARY KEY,
    FirstName VARCHAR(50) NOT NULL,
    LastName VARCHAR(50) NOT NULL,
    Email VARCHAR(100) NOT NULL UNIQUE,
    Date Of Birth DATE NOT NULL,
    Phone Number VARCHAR(20),
    Gender ENUM(Male, 'Female', 'Other', 'Prefer not to say')
    Address VARCHAR(255),
    City VARCHAR(100),
    State VARCHAR(100),
    ZipCode VARCHAR(20),
    Country VARCHAR(100),
    Registration Date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    IsActive BOOLEAN DEFAULT TRUE
    IsVerified BOOLEAN DEFAULT FALSE
);

4. Configure Database Connection
Update the database configuration in your backend code (typically in config.py or directly in crud.py).
Example configuration (MySQL):
python
DB_HOST = "localhost"
DB_USER = "your_username"
DB_PASSWORD = "your_password"
DB_NAME = "your_database"

5. Install Dependencies
Navigate to the backend directory and install the required Python packages:
bash
pip install -r requirements.txt

6. Run the Backend Server
In the backend directory, start the server:
bash
python crud.py
The server should now be running at http://localhost:5000.

Usage
API Endpoints
Create Registration

Endpoint: /register
Method: POST
Data: {"name": "Name", "email": "Email", "date_of_birth": "YYYY-MM-DD"}
Read Registration(s)

Endpoint: /register/{id} (GET a specific registration)
Endpoint: /registers (GET all registrations)
Update Registration

Endpoint: /register/{id}
Method: PUT
Data: {"name": "New Name", "email": "New Email", "date_of_birth": "YYYY-MM-DD"}
Delete Registration

Endpoint: /register/{id}
Method: DELETE
Error Handling
Each CRUD function handles basic errors, such as missing fields or invalid data types.
Database connection errors and invalid queries are also handled with appropriate error messages.
Contributing
Feel free to contribute by creating a pull request or by reporting any issues.

License 

This project is licensed under the GNU General Public License v3.0
