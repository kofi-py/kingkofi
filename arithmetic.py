""" This module provides functions to do basic arithmetic. """

def add(x, y):
    """ Return the sum of x and y. 
    
    Parameters: 
    x (number), y (number): The addends.

    Returns:
    number: The sum of x and y.
    """
    return x + y # addition

def subtract(x, y):
    return x - y # subtraction

def multiply(x, y):
    return x * y # multiplcation

def divide(x, y): # Careful here...
    try: # Use the try block to avoid error
        return x / y
    except ZeroDivisionError: # Ya can't divide by zero!!
        return 'Undefined' # Let's just say a message 'Undefined'

def power(x, y):
    return x ** y # exponent


