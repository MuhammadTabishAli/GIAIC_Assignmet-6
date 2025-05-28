class InvalidAgeError(Exception):
    """Raised when age is less than 18"""
    pass

def check_age(age):
    if age < 18:
        raise InvalidAgeError("Age must be 18 or above")
    print("Age is valid")

try:
    check_age(15)
except InvalidAgeError as e:
    print(f"Error: {e}")
else:
    print("No errors occurred")