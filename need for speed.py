number_of_cars = int(input())

car_info = {}

for _ in range(number_of_cars):
    info = input().split('|')

    car = info[0]
    mileage = int(info[1])
    fuel = int(info[2])
    car_info[car] = {'mileage': mileage, 'fuel': fuel}

command = input()

while command != 'Stop':
    commands = command.split(' : ')
    if commands[0] == "Drive":
        car = commands[1]
        distance = int(commands[2])
        fuel = int(commands[3])
        if car_info[car]['fuel'] - fuel >= 0:
            car_info[car]['mileage'] += distance
            car_info[car]['fuel'] -= fuel
            print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
        else:
            print("Not enough fuel to make that ride")
        if car_info[car]['mileage'] >= 100000:
            car_info.pop(car)
            print(f"Time to sell the {car}!")

    elif commands[0] == 'Refuel':
        car = commands[1]
        fuel = int(commands[2])
        current_fuel = car_info[car]['fuel']
        if car_info[car]['fuel'] + fuel > 75:
            car_info[car]['fuel'] = 75
            print(f"{car} refueled with {75 - current_fuel} liters")
        else:
            car_info[car]['fuel'] += fuel
            print(f"{car} refueled with {fuel} liters")
    elif commands[0] == "Revert":
        car = commands[1]
        kilometers = int(commands[2])
        if car_info[car]['mileage'] - kilometers < 10000:
            car_info[car]['mileage'] = 10000
        else:
            car_info[car]['mileage'] -= kilometers
            print(f"{car} mileage decreased by {kilometers} kilometers")

    command = input()

for key, value in car_info.items():
    print(f"{key} -> Mileage: {value['mileage']} kms, Fuel in the tank: {value['fuel']} lt.")
