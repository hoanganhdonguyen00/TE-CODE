def middle_char(s):
    sogiua = len(s) / 2
    if len(s) % 2 == 0:
        return s[sogiua - 1:sogiua + 1]
    else:
        return (sogiua)
middle_char()