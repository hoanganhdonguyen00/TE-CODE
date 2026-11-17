seasons = ( "spring", "summer", "autumn", "winter")
month = int(input("Enter the number of a month (1-12): "))
if 1 <= month <= 12:
    season_index = (month % 12) // 4
    print(f"The season is: {seasons[season_index]}")
else:
    print("Please enter number between 1 and 12.")