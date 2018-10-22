import random

random.seed()

board = []
mines = []
numbers = []
mine_count = 10


def print_board():
    print("   A B C D E F G H I J")
    print("   ___________________")
    counter = 0
    for x in board:
        print(str(counter)+" |", end="")
        for y in x:
            print(y, end=' ')
        print()
        counter += 1


def print_board_debug():
    print("   A B C D E F G H I J")
    print("   ___________________")
    counter = 0
    for x in mines:
        print(str(counter)+" |", end="")
        for y in x:
            print(y, end=' ')
        print()
        counter += 1


def print_board_numbers():
    print("   A B C D E F G H I J")
    print("   ___________________")
    counter = 0
    for x in numbers:
        print(str(counter)+" |", end="")
        for y in x:
            print(y, end=' ')
        print()
        counter += 1


def parse_command(command):
    command = command.split()

    if len(command) < 1:
        print("Please enter a command")
        return True

    elif command[0] == "print":
        if len(command) == 2 and command[1] == "debug":
            print_board_debug()
        elif len(command) == 2 and command[1] == "numbers":
            print_board_numbers()
        else:
            print_board()
        return True

    elif command[0] == "fire":
        if len(command) < 3:
            print("Error: fire command takes 2 coordinates.")
            return True
        if command[2].isnumeric():
            fire_at(command[1], int(command[2]))
            return True
        else:
            print("Error: fire command takes 2 coordinates.")
            return True

    elif command[0] == "quit":
        print("Thanks for playing!")
        return False

    else:
        print("Invalid command")
        return True


def fire_at(y, x):
    y = grid_to_num(y)
    if y in range(0, len(board)) and len(board) > 0 and x in range(0, len(board[0])):
        if mines[x][y] == "M":
            print("Game over!")
            exit()
    else:
        print("Specify a range within the board bounds")


def grid_to_num(value):
    result = -1
    if value == "A":
        result = 0
    elif value == "B":
        result = 1
    elif value == "C":
        result = 2
    elif value == "D":
        result = 3
    elif value == "E":
        result = 4
    elif value == "F":
        result = 5
    elif value == "G":
        result = 6
    elif value == "H":
        result = 7
    elif value == "I":
        result = 8
    elif value == "J":
        result = 9
    return result


def generate_mines():

    for i in range(10):
        mines.append([])
        for j in range(10):
            mines[i].append(".")

    for i in range(mine_count):
        x_val = random.randint(0, 9)
        y_val = random.randint(0, 9)
        mines[x_val][y_val] = "M"
        numbers[x_val][y_val] = "M"


def setup_board():
    for i in range(10):
        board.append([])
        for j in range(10):
            board[i].append(".")
    number_board()
    generate_mines()
    number_board_populate()


def number_board():
    for i in range(10):
        numbers.append([])
        for j in range(10):
            numbers[i].append("0")


def number_board_populate():
    for x in range(0, 10):
        for y in range(0, 10):
            counter = 0
            if x > 0 and y > 0:
                if mines[x-1][y-1] == "M":
                    counter += 1
            if y > 0:
                if mines[x][y-1] == "M":
                    counter += 1
            if y > 0 and x < 9:
                if mines[x+1][y-1] == "M":
                    counter += 1
            if x > 0:
                if mines[x-1][y] == "M":
                    counter += 1
            if mines[x][y] == "M":
                counter += 1
            if x < 9:
                if mines[x+1][y] == "M":
                    counter += 1
            if x > 0 and y < 9:
                if mines[x-1][y+1] == "M":
                    counter += 1
            if y < 9:
                if mines[x][y+1] == "M":
                    counter += 1
            if y < 9 and x < 9:
                if mines[x+1][y+1] == "M":
                    counter += 1
            if mines[x][y] == "M":
                numbers[x][y] = "M"
            else:
                numbers[x][y] = str(counter)
