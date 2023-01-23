number_of_pieces = int(input())

book_pieces = {}

for _ in range(number_of_pieces):
    pieces = input().split("|")
    piece = pieces[0]
    composer = pieces[1]
    key = pieces[2]

    book_pieces[piece] = {'composer': composer, 'key': key}

command = input()

while command != "Stop":
    commands = command.split("|")

    if commands[0] == "Add":
        piece = commands[1]
        composer = commands[2]
        key = commands[3]
        if piece not in book_pieces:
            book_pieces[piece] = {'composer': composer, 'key': key}
            print(f"{piece} by {composer} in {key} added to the collection!")
        else:
            print(f"{piece} is already in the collection!")

    elif commands[0] == "Remove":
        piece = commands[1]
        if piece in book_pieces:
            book_pieces.pop(piece)
            print(f"Successfully removed {piece}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")
    elif commands[0] == "ChangeKey":
        piece = commands[1]
        new_key = commands[2]
        if piece in book_pieces:
            book_pieces[piece]['key'] = new_key
            print(f"Changed the key of {piece} to {new_key}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection!")

    command = input()

for key, value in book_pieces.items():

    print(f"{key} -> Composer: {value['composer']}, Key: {value['key']}")
