#!/usr/bin/env python3
"""Filtered logger module"""
import re


def filter_datum(fields, redaction, message, separator):
    """Obfuscate specified fields in a log message"""
    pattern = r'({})=[^{}]*'.format('|'.join(fields), separator)
    return re.sub(pattern, lambda m: m.group(1) + '=' + redaction, message)
