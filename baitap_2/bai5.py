def s(diameter, price):
    area = 3.14 * ((diameter / 200) ** 2)
DODAI1 = float(input("Diameter 1: "))
GIA1 = float(input("Price 1: "))
DODAI2 = float(input("Diameter 2: "))
GIA2 = float(input("Price 2: "))
first_pizza = (DODAI1, GIA1)
second_pizza = (DODAI2, GIA2 )
cal1 = GIA1/DODAI1
cal2 = GIA2/DODAI2
if first_pizza < second_pizza:
    print("Pizza 1 is better.")
else:
    print("Pizza 2 is better.")