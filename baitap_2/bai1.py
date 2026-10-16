def size():
    length = float(input("Enter the size of fish: "))
    if length < 42:
        print("Please release the fish into the lake.")
        print(f"The fish only have {length} cm.")
    else:
        print("It long enough.")
size()