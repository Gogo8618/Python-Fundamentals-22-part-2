number = int(input())
heroes_info = {}
for _ in range(number):
    heroes = input().split(' ')
    name = heroes[0]
    HP = int(heroes[1])
    MP = int(heroes[2])
    heroes_info[name] = {'HP': HP, 'MP': MP}

command = input()

while command != "End":
    items = command.split(' - ')

    if items[0] == "CastSpell":
        name = items[1]
        MP = int(items[2])
        spell_name = items[3]

        if heroes_info[name]['MP'] - MP < 0:
            print(f"{name} does not have enough MP to cast {spell_name}!")
        else:
            heroes_info[name]['MP'] -= MP
            print(f"{name} has successfully cast {spell_name} and now has {heroes_info[name]['MP']} MP!")

    elif items[0] == 'TakeDamage':
        name = items[1]
        damage = int(items[2])
        attacker = items[3]
        if heroes_info[name]['HP'] - damage <= 0:
            print(f"{name} has been killed by {attacker}")
        else:
            heroes_info[name]['HP'] -= damage
            print(f"{name} was hit for {damage} HP by {attacker} and now has {heroes_info[name]['HP']} HP left!")
    elif items[0] == 'Recharge':
        name = items[1]
        amount = int(items[2])
        current_MP = heroes_info[name]['MP']
        if heroes_info[name]['MP'] + amount > 200:
            heroes_info[name]['MP'] = 200
            print(f"{name} recharged for {200 - current_MP} MP!")
        else:
            heroes_info[name]['MP'] += amount
            print(f"{name} recharged for {amount} MP!")
    elif items[0] == 'Heal':
        name = items[1]
        amount = int(items[2])
        current_HP = heroes_info[name]['HP']
        if heroes_info[name]['HP'] + amount > 100:
            heroes_info[name]['HP'] = 100
            print(f"{name} recharged for {100 - current_HP} HP!")
        else:
            heroes_info[name]['HP'] += amount
            print(f"{name} healed for {amount} HP!")

    command = input()

for key, value in heroes_info.items():
    print(f"{key}\n HP: {value['HP']}\n MP: {value['MP']}")
