#!/usr/bin/python3
# 3-safe_print_division.py
# Benjamin Alfayo

def safe_print_division(a, b):
    """Returns the exact divisin of a by b."""
    try:
        div = a / b
    except (TypeError, ZeroDivisionError):
        div = None
    finally:
        print("Inside result: {}".format(div))
    return (div)
