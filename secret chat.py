concealed_message = input()

command = input()

while command != "Reveal":

    items = command.split(':|:')
    if items[0] == 'InsertSpace':
        index = int(items[1])
        concealed_message = concealed_message[:index] + ' ' + concealed_message[index:]
    elif items[0] == 'Reverse':
        substring = items[1]
        reverse_substring = substring[::-1]
        if substring in concealed_message:
            concealed_message = concealed_message.replace(substring, '', 1)
            concealed_message = concealed_message[0:len(concealed_message)] + reverse_substring
        else:
            print('error')
    elif items[0] == 'ChangeAll':
        substring = items[1]
        replacement = items[2]
        concealed_message = concealed_message.replace(substring, replacement)

    command = input()
print(concealed_message)