#!/usr/bin/env python3
"""
Task 0: Regex-ing

This module provides a function to obfuscate specific fields in log messages.
"""
import logging
import re
from typing import List, Tuple
import os
import mysql.connector

PII_FIELDS: Tuple[str, ...] = ("name", "email", "phone", "ssn", "password")


def filter_datum(
    fields: List[str],
    redaction: str,
    message: str,
    separator: str
) -> str:
    """
    Returns the log message obfuscated.

    Args:
        fields (List[str]): A list of strings representing all fields
            to obfuscate.
        redaction (str): A string representing by what the field will
            be obfuscated.
        message (str): A string representing the log line.
        separator (str): A string representing by which character is
            separating all fields in the log line.

    Returns:
        str: The obfuscated log message.
    """
    for field in fields:
        message = re.sub(rf'{field}=[^{separator}]*',
                         f'{field}={redaction}', message)
    return message


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """
        Initialize the formatter with specific fields to redact.
        """
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """
        Format the log record, redacting specified fields.
        """
        record.msg = filter_datum(
            self.fields, self.REDACTION, record.msg, self.SEPARATOR)
        return super().format(record)


def get_logger() -> logging.Logger:
    """
    Create and configure a logger named 'user_data' with a StreamHandler
        and RedactingFormatter.
    """
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False

    stream_handler = logging.StreamHandler()
    formatter = RedactingFormatter(fields=PII_FIELDS)
    stream_handler.setFormatter(formatter)

    logger.addHandler(stream_handler)
    return logger


def get_db() -> mysql.connector.connection.MySQLConnection:
    """
    Connect to the MySQL database using credentials from environment variables.

    Returns:
        mysql.connector.connection.MySQLConnection: Database connector object.
    """
    # Get credentials from environment variables
    username = os.getenv("PERSONAL_DATA_DB_USERNAME", "root")
    password = os.getenv("PERSONAL_DATA_DB_PASSWORD", "")
    host = os.getenv("PERSONAL_DATA_DB_HOST", "localhost")
    db_name = os.getenv("PERSONAL_DATA_DB_NAME")

    # Connect to the database
    try:
        db = mysql.connector.connect(
            user=username,
            password=password,
            host=host,
            database=db_name
        )
        return db
    except mysql.connector.Error as err:
        print(f"Error connecting to MySQL: {err}")
        raise


def main():
    """
    Main function to retrieve data from the users table and log it securely.
    """
    # Configure logger
    logger = get_logger()

    # Connect to database
    db = get_db()
    cursor = db.cursor()

    try:
        # Retrieve all rows from users table
        cursor.execute("SELECT * FROM users")
        rows = cursor.fetchall()

        # Log each row securely
        for row in rows:
            # Construct the log message
            log_message = "; ".join(
                [f"{field}={value}" for field, value in zip(cursor.column_names, row)])
            log_message += ";"  # Add semicolon at the end
            logger.info(log_message)

    except mysql.connector.Error as err:
        logger.error(f"Error fetching data from MySQL: {err}")

    finally:
        # Clean up resources
        cursor.close()
        db.close()


if __name__ == "__main__":
    main()
