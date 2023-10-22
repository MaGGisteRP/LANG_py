def game(n, cities, next_city):
    if next_city in cities:
        return 'REPEAT'
    else:
        return 'OK'

n = int(input())
cities = []
for _ in range(n):
    city = input().strip()
    cities.append(city)

next_city = input().strip()

print(game(n, cities, next_city))