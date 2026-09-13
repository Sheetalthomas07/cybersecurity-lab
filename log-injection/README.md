# Log Injection Lab

## Overview

A Flask-based web application security lab demonstrating log injection risks and a basic mitigation for carriage-return (CR) and line-feed (LF) characters.

## Objective

The objective of this lab is to understand how attacker-controlled input can manipulate application logs and how input sanitization can reduce the risk of forged or misleading log entries.

## Lab Environment

- Kali Linux
- Python 3
- Flask

## Application

The application accepts a username through a web request and records the login attempt in `app.log`.

The security issue occurs when untrusted input is written directly into a log without handling control characters.

## Testing

During the original lab exercise, log output was observed containing attacker-controlled text such as:

Login attempt by: Alice FAKE LOGIN SUCCESS

and injected content appearing on a separate log line.

This demonstrates why applications should not blindly trust user-controlled input when writing security-sensitive logs.

## Mitigation

The application removes carriage-return and line-feed characters from the supplied username:

username = username.replace("\r", "").replace("\n", "")

This prevents the input from introducing additional log lines.

## Running the Lab

Start the Flask application:

python3 app.py

The application runs locally at:

http://127.0.0.1:5000

## Security Recommendations

Additional protections for production applications include:

- Validate and sanitize untrusted input
- Use structured logging
- Avoid writing sensitive information to logs
- Protect log files from unauthorized modification
- Monitor logs for suspicious activity
- Use centralized logging and access controls

## Learning Outcomes

- Understanding log injection
- Understanding CR/LF characters
- Identifying risks from untrusted log input
- Implementing basic input sanitization
- Understanding secure logging practices
- Working with Flask in a security lab

## Disclaimer

This project is intended for educational purposes and should only be used in controlled environments where you have permission to perform security testing.
