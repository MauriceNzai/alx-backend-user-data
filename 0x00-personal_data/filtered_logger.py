#!/usr/bin/env python3
"""
function called filter_datum that returns the log message obfuscated
"""

from typing import List
import re


patterns = {
    'extract': lambda x, y: r'(?P<field>{})=[^{}]*'.format('|'.join(x), y),
    'replace': lambda x: r'\g<field>={}'.format(x),
}

def filter_datum(
        fields: List[str], redaction: str, message: str, separator: str,
        ) -> str:
    """
    filters a log line and returns the log message
    Arguments:
        fields: a list of strings representing all fields to obfuscate
        redaction: a string representing by what the field will be obfuscated
        message: a string representing the log line
        separator: a string representing the character separating fields in log
    """
    extract, replace = (patterns["extract"], patterns["replace"])
    return re.sub(extract(fields, separator), replace(redaction), message)
