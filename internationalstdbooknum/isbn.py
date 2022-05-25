import re

def is_valid_isbn(code):
    code = code.replace("-", "").replace(" ", "")
    
    return {
        10: is_valid_isbn10,
        13: is_valid_isbn13
    }.get(len(code), lambda n: False)(code)


def isOdd(x):
    return x % 2 != 0


def calcCheckDigit(code):
    result = -1
    code.replace("-", "").replace(" ", "")
    sum = 0

    for i in range(len(code)):
        digit = int(code[i])
        sum += digit * (3 if isOdd(i) else 1)

    result = (10 - sum % 10) % 10

    return result


def is_valid_isbn10(code):
    result = 0

    if re.match('^\d{9}[\d,X]{1}$', code):
        sum = 0

        for i in range(9):
            sum += int(code[i]) * (10 - i)

        if code[9].lower() == 'x':
            sum += 10 
        
        else: 
            sum += int(code[9])

        result = sum % 11 == 0

        if result:
            print("Valid")
            code = code[:len(code) - 1]

            result = "978" + code
            result += str(calcCheckDigit(result))

            if is_valid_isbn13(result):
                print(result)
                return result
        
        else:
            print("Invalid")

def is_valid_isbn13(code):
    result = 0

    if re.match('^\d{13}$', code):
        sum = 0

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

value = input("Please enter your ISBN: ")
is_valid_isbn(value)