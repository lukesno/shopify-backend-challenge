# Custom exceptions for error checking

class DeletionError(Exception):
    """Exception raised when deleted item is attempted to be deleted again"""
    def __init__(self, message="Item is already deleted. You cannot delete an item twice."):
        self.message = message

    def __str__(self):
        return(self.message)

class InvalidInputError(Exception):
    """Exception raised when item is attempted to be updated/created with invalid input"""
    def __init__(self, message="Invalid input was provided. Please try again."):
        self.message = message

    def __str__(self):
        return(self.message)

class RetrievalError(Exception):
    """Exception raised when items are retrieved with an invalid type"""
    def __init__(self, message="Invalid endpoint for retrival. Please try again."):
        self.message = message

    def __str__(self):
        return(self.message)

class InvalidDataFound(Exception):
    """Exception raised when invalid data is encountered from database"""
    def __init__(self, message="Invalid data was found in database. This is very unsafe! Contact the admin."):
        self.message = message

    def __str__(self):
        return(self.message)

class EmptyResultSet(Exception):
    """Exception raised when SELECT query returned with no results"""
    def __init__(self, message="No items were found."):
        self.message = message

    def __str__(self):
        return(self.message)

class RestorationError(Exception):
    """Exception raised when revived item is attempted to be revived again"""
    def __init__(self, message="Item is already restored. You cannot restore an item twice."):
        self.message = message

    def __str__(self):
        return(self.message)