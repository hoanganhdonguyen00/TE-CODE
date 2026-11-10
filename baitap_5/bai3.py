# city1 = input("nhập thành phố 1: ")
# city2 = input("nhập thành phố 2: ")
# city3 = input("nhập thành phố 3: ")
# city4 = input("nhập thành phố 4: ")
# city5 = input("nhập thành phố 5: ")
# city = [city1, city2, city3, city4, city5 ]
# for x in city:
#     print(x)

cities = []
for i in range(5):
    city_name = input(f"Enter city, {i + 1} ")
    cities.append(city_name)
for city in cities:
    print(city)