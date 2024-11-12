# CRUD
This repository contains a simple CRUD (Create, Read, Update, Delete) application that manages user registrations. The application uses an SQL database to store and retrieve registration data, with fields such as ID, Name, Email, and Date of Birth.

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
SQL Database (MySQL or PostgreSQL)
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
    ID INT PRIMARY KEY AUTO_INCREMENT,
    Name VARCHAR(50) NOT NULL,
    Email VARCHAR(100) UNIQUE NOT NULL,
    DateOfBirth DATE NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

3. Configure Database Connection
Update the database configuration in your backend code (typically in config.py or directly in crud.py).
Example configuration (MySQL):
python
DB_HOST = "localhost"
DB_USER = "your_username"
DB_PASSWORD = "your_password"
DB_NAME = "your_database"

4. Install Dependencies
Navigate to the backend directory and install the required Python packages:
bash
pip install -r requirements.txt

5. Run the Backend Server
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
This project is licensed under the MIT License.
