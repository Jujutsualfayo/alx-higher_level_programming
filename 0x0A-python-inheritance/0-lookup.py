#!/usr/bin/python3
# 0-lookup.py
# Benjamin Alfayo
"""Defines an exact  object attribute lookup function."""


def lookup(obj):
    """Return a list of an object's available attributes."""
    return (dir(obj))
