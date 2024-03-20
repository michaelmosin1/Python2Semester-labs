n = int(input())
cities = []
for i in range(n):
    city = input()
    if city not in cities:
        cities.append(city)
        print("OK")
    else:
        print("REPEAT")
