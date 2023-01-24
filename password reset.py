password = input()
sub_password = password

command = input()

while command != "Done":
    commands = command.split(' ')
    if commands[0] == "TakeOdd":
        current_password = sub_password
        sub_password = ''

        for i in range(len(current_password)):
            if i % 2 != 0:
                sub_password += current_password[i]
        print(sub_password)
    elif commands[0] == "Cut":
        index = int(commands[1])
        length = sub_password[index:index + int(commands[2])]
        sub_password = sub_password.replace(length, '', 1)
        print(sub_password)
    elif commands[0] == "Substitute":
        substring = commands[1]
        substitute = commands[2]
        if substring in sub_password:
            sub_password = sub_password.replace(substring, substitute)
            print(sub_password)
        else:
            print("Nothing to replace!")
    command = input()

print(f"Your password is: {sub_password}")



