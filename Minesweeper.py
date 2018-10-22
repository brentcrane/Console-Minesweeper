import Functions as Func

running = True
Func.setup_board()

while running:
    user_command = input("> ")
    result = Func.parse_command(user_command)
    if not result:
        running = False
