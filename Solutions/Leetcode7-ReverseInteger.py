def reverse(x):
    reverse = []
    res = ''

    if x < 0:
        num =  list(str(abs(x)))
       
        for i in num:
            reverse.insert(0, i)

        for i in reverse:
            res += i
        if -2**31 <= int(res) <= 2**31 - 1:
            return 0 - int(res)

    elif x > 0:
        num =  list(str(abs(x)))
       
        for i in num:
            reverse.insert(0, i)

        for i in reverse:
            res += i

        if -2**31 <= int(res) <= 2**31 - 1:
            return int(res)

    return 0

print(reverse(123))
print(reverse(-123))
print(reverse(120))
print(reverse(1534236469))
