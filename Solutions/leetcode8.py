def myAtoi(s):
    INT_MAX, INT_MIN = 2**31 - 1, -2**31
    s = s.strip()
    result, i, n = 0, 0, len(s)

    sign = 1
    if i < n and s[i] == '-':
        sign = -1 # neg num
        i += 1 # to ignore the sign in while
    elif i < n and s[i] == '+':
        i += 1

    while i < n and s[i].isdigit():
        digit = int(s[i])
        if result > (INT_MAX - digit) // 10:
            return INT_MAX if sign == 1 else INT_MIN
        result = result * 10 + digit
        i += 1
    
    return sign * result

print(myAtoi("42"))
print(myAtoi("   -042"))
print(myAtoi("1337c0d3"))
print(myAtoi("-+12"))
print(myAtoi("words and 987"))