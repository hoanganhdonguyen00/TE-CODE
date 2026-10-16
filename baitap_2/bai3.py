def s():
    sex = input("Enter your biological: ")
    hemoglobin_value = int(input("Enter your hemoglobin value: "))
    if sex == "female":
        if hemoglobin_value < 117:
            print("low")
        elif hemoglobin_value > 155:
            print("high")
        else:
            print("normal")
    elif sex == "male":
        if hemoglobin_value < 134:
            print("low")
        elif hemoglobin_value > 167:
            print("Hhigh")
        else:
            print("normal")
s()