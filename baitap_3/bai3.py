a = input("Nhập số: ")
nho_nhat = lon_nhat = float(a)

while a != "":
    a = float(a)
    if a < nho_nhat:
        nho_nhat = a
    if a > lon_nhat:
        lon_nhat = a
    a = input("Nhập số: ")

print(f"Nhỏ nhất: {nho_nhat}, Lớn nhất: {lon_nhat}")