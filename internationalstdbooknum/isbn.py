import re

def is_valid_isbn(code):
    # replace characters and spaces with no value strings
    code = code.replace("-", "").replace(" ", "")
    
    # Figure out which function to run based on ISBN length
    return {
        10: is_valid_isbn10,
        13: is_valid_isbn13
    }.get(len(code), lambda n: False)(code)

# Determine wheher an index position is odd or even
def isOdd(x):
    return x % 2 != 0

# calculate the check digit for converting ISBN-10 to ISBN-13
def calcCheckDigit(code):
    result = -1
    code.replace("-", "").replace(" ", "")
    sum = 0

    for i in range(len(code)):
        digit = int(code[i])
        sum += digit * (3 if isOdd(i) else 1)

    result = (10 - sum % 10) % 10

    return result

# Function for validating ISBN-10
def is_valid_isbn10(code):
    result = 0

    # Using regex to filter through the characters in the string and determine whether
    # they're numbers or X
    if re.match('^\d{9}[\d,X]{1}$', code):
        sum = 0

        # Loop through the numbers and multiply them by their corresponding positions [0] by 10, [1] by 9...
        for i in range(9):
            sum += int(code[i]) * (10 - i)

        # Handling if the last character in the string is X
        if code[9].lower() == 'x':
            sum += 10 
        
        else: 
            sum += int(code[9])

        result = sum % 11 == 0
        
        # Validating ISBN-10 and converting to ISBN-13
        if result:
            print("Valid")
            code = code[:len(code) - 1]

            result = "978" + code
            result += str(calcCheckDigit(result))

            # Checking if the converted ISBN-13 code is valid
            if is_valid_isbn13(result):
                print(result)
                return result
        
        else:
            print("Invalid")

# Function for validating ISBN-13
def is_valid_isbn13(code):
    result = 0

    # Checking that all characters are numbers
    if re.match('^\d{13}$', code):
        sum = 0

        # Multiplying values by 1 if index position is even and 3 if index position is odd
        for i in range(len(code)):
            digit = int(code[i])
            sum += digit * (3 if isOdd(i) else 1)

        result = sum % 10 == 0

    if result:
        print("Valid")
        return result
    
    else:
        print("Invalid")
        return result

# Enabling input of ISBN code through CLI
value = input("Please enter your ISBN: ")
is_valid_isbn(value)