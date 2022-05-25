# Code Test
---

## Commands to run
- docker-compose build
- docker run -ti hyperiontht
- Follow prompts

---

## Worst-case space complexity
I would argue that this solution follows the linear complexity and is thus O(n).

### Example 
```
def is_valid_isbn13(code):
    result = 0

    # Checking that all characters are numbers
    if re.match('^\d{13}$', code):
        sum = 0

        # Multiplying values by 1 if index position is even and 3 if index position is odd
        for i in range(len(code)):
            digit = int(code[i])
            sum += digit * (3 if is_odd(i) else 1)

        result = sum % 10 == 0

    if result:
        print('Valid')
        return result
    
    else:
        print('Invalid')
        return result
```


In the above-given code, the array consists of n integer elements. So, the space occupied by the array is 4 * n. Also we have integer variables such as n, i and sum. Assuming 4 bytes for each variable, the total space occupied by the program is 4n + 16 bytes. Since the highest order of n in the equation 4n + 16 is n, so the space complexity is O(n) or linear.

 