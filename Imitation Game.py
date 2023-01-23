encrypted_message = input()

command = input()

while command != "Decode":
    message = command.split('|')

    if message[0] == "Move":
        number_of_letters = int(message[1])
        encrypted_message = encrypted_message[number_of_letters:] + encrypted_message[:number_of_letters]
    elif message[0] == "Insert":
        index = int(message[1])
        value = message[2]
        encrypted_message = encrypted_message[:index] + value + encrypted_message[index:]
    elif message[0] == "ChangeAll":
        old = message[1]
        new = message[2]
        encrypted_message = encrypted_message.replace(old, new)
    command = input()

print(encrypted_message)
