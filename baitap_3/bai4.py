import random
s = random.randint(1, 10)
a = int(input("Chọn số: "))

while a != s:
    if a > s:
        print("cao qá")
    else:
        print("thấp qá")
    a = int(input("Đoán lại: "))
print("đroi")