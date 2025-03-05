## In python we can define custom exceptions by creating a new class that is derived from the buil-in Exception class

class CustomException(Exception):
    "Raised when person age is less than 18"
    pass
try:
    age =int(input('Enter the age: '))
    if (age<18):
        raise CustomException
except CustomException:
    print('Person is not eligible to vote')
else:
    print("person is eligible for voting")
    


import sys  # Importing sys module
from custom_exceptions import InvalidAgeError  # Importing custom exception

class AgeValidator:
    """A class to validate age input."""

    @staticmethod
    def check_age(age):
        """Checks if age is within the valid range."""
        if age < 18 or age > 60:
            raise InvalidAgeError(age)  # Raising custom exception
        else:
            print("Age is valid")

if __name__ == "__main__":
    try:
        age = int(input("Enter your age: "))  # User input
        AgeValidator.check_age(age)  # Calling method

    except InvalidAgeError as e:  
        print(f"Custom Exception Caught: {e}")  # Printing custom error message
        sys.exit(1)  # Exiting program safely

    except ValueError:  
        print("Invalid input! Please enter a number.")  
        sys.exit(1)  # Exiting due to invalid input

    except Exception as e:
        print(f"Unexpected Error: {sys.exc_info()[0]} - {e}")  # sys.exc_info() gives error type
        sys.exit(1)  # Exit program
