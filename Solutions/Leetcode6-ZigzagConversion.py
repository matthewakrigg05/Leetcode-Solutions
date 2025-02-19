def convert(s, numRows):
    if numRows == 1 or len(s) < numRows:
        return s

    rows = [''] * numRows  # creates a string for each row
    index, step = 0, 1  # starts at first row, increases by ste

    for char in s:
        rows[index] += char  # first iteration adds first char to first row

        if index == 0:  # once reaching zero, the zig is going down direction
            step = 1
        elif index == numRows - 1:  # when reaches nrows - 1, starts going back through the rows in reverse
            step = -1

        index += step

    return ''.join(rows)


print(convert("PAYPALISHIRING", 4))
print(convert("PAYPALISHIRING", 3))
print(convert("A", 1))
