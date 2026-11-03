import re
def s(text):
    số = re.findall(r"\d+",text )
    tổng =0
    for num in số:
        tổng = tổng + int(num)
    return tổng
check = "today 11/3/2026"
print(s(check))