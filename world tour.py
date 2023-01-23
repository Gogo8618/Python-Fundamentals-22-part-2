stops = input()

command = input()

while command != "Travel":

    items = command.split(':')
    if items[0] == "Add Stop":
        index = int(items[1])
        value = items[2]
        if 0 < index < len(stops):
            stops = stops[:index] + value + stops[index:]
            print(stops)
    elif items[0] == "Remove Stop":
        start = int(items[1])
        end = int(items[2])
        if 0 < start < len(stops) and 0 < end < len(stops):
            stops = stops[:start] + stops[end + 1:]
            print(stops)

    elif items[0] == "Switch":
        old_string = items[1]
        new_string = items[2]
        stops = stops.replace(old_string, new_string)
        print(stops)

    command = input()

print(f"Ready for world tour! Planned stops {stops}")
