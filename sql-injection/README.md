# SQL Injection Lab

## Overview

A Flask-based web application security lab focused on SQL injection and its mitigation using parameterized queries.

## Objective

The objective of this lab is to understand how insecure SQL queries can expose applications to SQL injection and how parameterized queries can prevent this vulnerability.

## Lab Environment

- Kali Linux
- Python 3
- Flask
- SQLite

## Application Structure

.
├── app.py
├── setup_db.py
└── README.md

## Database Setup

setup_db.py creates a SQLite database containing a users table with test credentials for the lab.

Run:

python3 setup_db.py

## Security Implementation

The application uses a parameterized SQL query with placeholders:

SELECT * FROM users
WHERE username = ? AND password = ?

User input is supplied separately to the SQL statement:

cursor.execute(query, (username, password))

This prevents user-controlled input from being interpreted as part of the SQL statement.

## Running the Application

Start the Flask application:

python3 app.py

The application runs locally at:

http://127.0.0.1:5002

## Mitigation

The primary mitigation demonstrated in this lab is the use of parameterized queries (prepared statements) instead of constructing SQL queries by concatenating user input.

Additional security measures include:

- Input validation
- Strong password hashing
- Least-privilege database access
- Secure error handling
- Avoiding sensitive information in application responses

## Learning Outcomes

- Understanding the basic concept of SQL injection
- Understanding why insecure SQL queries are dangerous
- Understanding parameterized queries
- Implementing SQL injection mitigation
- Working with Flask and SQLite
- Building a basic web security lab

## Disclaimer

This project is intended for educational purposes and should only be used in controlled environments where you have permission to perform security testing.
