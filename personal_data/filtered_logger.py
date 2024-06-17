#!/usr/bin/env python3
"""
Task 0: Regex-ing

This module provides a function to obfuscate specific fields in log messages.
"""
import logging
import re
from typing import List



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
