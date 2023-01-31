CITIES = {}

while True:
    user_input = input("Enter a city: ").strip()
    if user_input:
        precip = input("Enter rain amount:").strip()
        if user_input in CITIES:
            CITIES[user_input] += int(precip)
        else:
            CITIES[user_input] = int(precip)
    else:
        break

for city, rainfall in CITIES.items():
    print(f'{city}: {rainfall:5}')
