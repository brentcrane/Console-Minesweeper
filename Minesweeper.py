import random

# Seed the random number generator
random.seed()

board = []
board_debug = []
mine_count = 0


# Initialize and print the game board
def game_init():
    setup_board()
    print_board(["print"])


# Determine which command is being called
def parse_command(command):
    command_list = command.split()
    if command_list[0] == "print":
        print_board(command_list)
    elif command_list[0] == "fire":
        fire(command_list)
    elif command_list[0] == "quit":
        end_game()
    elif command_list[0] == "flag":
        flag(command_list)
    else:
        print("Invalid command")


# Print the board, either in normal or debug mode
def print_board(command):
    if len(command) > 1 and command[1] == "debug":
        print("   A B C D E F G H I J")
        print("   ___________________")
        counter = 0
        for x in board_debug:
            print(str(counter) + " |", end="")
            for y in x:
                print(y, end=' ')
            print()
            counter += 1
    else:
        print("   A B C D E F G H I J")
        print("   ___________________")
        counter = 0
        for x in board:
            print(str(counter) + " |", end="")
            for y in x:
                print(y, end=' ')
            print()
            counter += 1


# End the game
def end_game():
    print("Game over. Thanks for playing!")
    exit(0)


# Error-checking wrapper of fire command
def fire(command):
    if len(command) < 3:
        print("Error: fire command takes 2 coordinates.")
    elif command[2].isnumeric():
        column = ord(command[1])-65
        if 0 <= column <= 9:
            fire_at_grid(column, command[2])
        else:
            print("Enter a valid column value. Caps only. (A-J)")
    else:
        print("Error: fire command takes 2 coordinates.")


# Flag a space as a possible mine-spot
def flag(command):
    if len(command) < 3:
        print("Error: flag command takes 2 coordinates.")
    elif command[2].isnumeric():
        # Converts the A-J value to a numeric value
        column = ord(command[1])-65
        if 0 <= column <= 9:
            board[int(command[2])][int(column)] = "X"
        else:
            print("Enter a valid column value. Caps only. (A-J)")
    else:
        print("Error: flag command takes 2 coordinates.")
    print_board(["print"])


# Fire at a specific spot on the board
def fire_at_grid(y, x):
    y = int(y)
    x = int(x)
    target = board_debug[x][y]
    if target == "M":
        board[x][y] = target
        print_board(["print", "debug"])
        end_game()
    elif target == "0":
        board[x][y] = target
        flood_fill(x, y)
        print_board(["print"])
    elif target.isnumeric():
        board[x][y] = target
        print_board(["print"])


# Recursive algorithm that opens up any adjacent empty spaces, and
# displays the numbers around the perimeter of the open space
def flood_fill(x, y):
    # If the spot is a zero, check its neighbors
    if board_debug[x][y] == "0":
        board[x][y] = "0"
        # Adjacent tiles
        if y-1 >= 0 and (board[x][y-1] == "." or board[x][y-1] == "X"):
            flood_fill(x, y-1)
        if y+1 <= 9 and (board[x][y+1] == "." or board[x][y+1] == "X"):
            flood_fill(x, y+1)
        if x-1 >= 0 and (board[x-1][y] == "." or board[x-1][y] == "X"):
            flood_fill(x-1, y)
        if x+1 <= 9 and (board[x+1][y] == "." or board[x+1][y] == "X"):
            flood_fill(x+1, y)
        # Diagonal tiles
        if x-1 >= 0 and y-1 >= 0 and (board[x-1][y-1] == "." or board[x-1][y-1] == "X"):
            flood_fill(x-1, y-1)
        if x-1 >= 0 and y+1 <= 9 and (board[x-1][y+1] == "." or board[x-1][y+1] == "X"):
            flood_fill(x-1, y+1)
        if x+1 <= 9 and y-1 >= 0 and (board[x+1][y-1] == "." or board[x+1][y-1] == "X"):
            flood_fill(x+1, y-1)
        if x+1 <= 9 and y+1 <= 9 and (board[x+1][y+1] == "." or board[x+1][y+1] == "X"):
            flood_fill(x+1, y+1)
    # If the spot is not a zero, display its number value
    else:
        board[x][y] = board_debug[x][y]


# Create both the normal and the debug board
def setup_board():
    global mine_count
    # Create the debug board (debug board is a bad name)
    for i in range(10):
        board.append([])
        board_debug.append([])
        for j in range(10):
            board[i].append(".")
            if random.randint(0, 100) < 25:
                mine_count += 1
                board_debug[i].append("M")
            else:
                board_debug[i].append(".")
    # Create the playing board, and count how many mines were generated
    for x in range(0, 10):
        for y in range(0, 10):
            counter = 0
            if x > 0 and y > 0:
                if board_debug[x - 1][y - 1] == "M":
                    counter += 1
            if y > 0:
                if board_debug[x][y - 1] == "M":
                    counter += 1
            if y > 0 and x < 9:
                if board_debug[x + 1][y - 1] == "M":
                    counter += 1
            if x > 0:
                if board_debug[x - 1][y] == "M":
                    counter += 1
            if board_debug[x][y] == "M":
                counter += 1
            if x < 9:
                if board_debug[x + 1][y] == "M":
                    counter += 1
            if x > 0 and y < 9:
                if board_debug[x - 1][y + 1] == "M":
                    counter += 1
            if y < 9:
                if board_debug[x][y + 1] == "M":
                    counter += 1
            if y < 9 and x < 9:
                if board_debug[x + 1][y + 1] == "M":
                    counter += 1
            if board_debug[x][y] != "M":
                board_debug[x][y] = str(counter)


# Game Loop and initialization
game_init()
while True:
    user_command = input("> ")
    parse_command(user_command)

