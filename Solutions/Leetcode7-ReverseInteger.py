def reverse(x):
    if x != 0:
        res = ''
        num = list(str(abs(x)))

        for i in num[::-1]:
            res += str(i)

        if -2 ** 31 <= int(res) <= 2 ** 31 - 1: # constraint outlined in the problem description, must be 32-bit int
            if x < 0: # handling for original case of num being negative or not
                return 0 - int(res)
            else:
                return int(res)
                
        return 0

print(reverse(123))
print(reverse(-123))
print(reverse(120))
print(reverse(1534236469))
