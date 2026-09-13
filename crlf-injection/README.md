# CRLF Injection Lab

## Overview

A Flask-based web application security lab demonstrating CRLF injection risks and a basic mitigation for carriage-return (CR) and line-feed (LF) characters.

## Objective

The objective of this lab is to understand how CRLF characters in user-controlled input can affect HTTP-related data and how sanitizing these characters can reduce injection risks.

## Lab Environment

- Kali Linux
- Python 3
- Flask

## Application

The application accepts a user-controlled value and uses it to construct a simulated HTTP-style response header.

The security risk occurs when untrusted input containing CR (`\r`) or LF (`\n`) characters is used without validation or sanitization.

## Mitigation

The application removes carriage-return and line-feed characters from user input:

value = value.replace("\r", "").replace("\n", "")

This prevents the supplied value from introducing additional lines into the simulated response.

## Running the Lab

Start the Flask application:

python3 app.py

The application runs locally at:

http://127.0.0.1:5001

## Security Recommendations

Additional protections include:

- Validate user-controlled input
- Reject unexpected control characters
- Use framework-provided response/header APIs
- Avoid constructing HTTP headers directly from untrusted input
- Apply appropriate output encoding
- Keep security-sensitive response values under strict application control

## Learning Outcomes

- Understanding CRLF injection
- Understanding carriage-return and line-feed characters
- Understanding how untrusted input can affect HTTP-related data
- Implementing basic CR/LF sanitization
- Working with Flask and HTTP concepts
- Understanding secure input handling

## Disclaimer

This project is intended for educational purposes and should only be used in controlled environments where you have permission to perform security testing.
