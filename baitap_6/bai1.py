numbers = []
while True:
    user_input = input("Enter a number: ")
    if user_input == "":
        break
    try:
        numbers.append(float(user_input))
    except ValueError:
        print("Please just enter a number.")
numbers.sort(reverse=True)
print("5 largest numbers:")
for num in numbers[:5]:
    print(num)