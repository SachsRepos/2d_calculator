print("Terminal. Type 'view list' to see list of commands.")
terminal = ""
while terminal.upper() != "QUIT":
    terminal = input("- ")
    if terminal.upper() == "VIEW LIST":
        print("""
    start addition - Add 2 addends.
    start subtraction - Subtract the subtrahend from the minuend.
    start multiplication - Multiply the multiplicand with the multiplier.
    start division - Divide the dividend by the divisor.
    quit - Exit the program
    """)
    elif terminal.upper() == "START ADDITION":
        add_1 = input("1st addend- ")
        add_2 = input("2nd addend- ")
        add_result = int(add_1) + int(add_2)
        print(add_result)
    elif terminal.upper() == "START SUBTRACTION":
        sub_1 = input("Minuend- ")
        sub_2 = input("Subtrahend- ")
        sub_result = int(sub_1) - int(sub_2)
        print(sub_result)
    elif terminal.upper() == "START MULTIPLICATION":
        mul_1 = input("Multiplicand- ")
        mul_2 = input("Multiplier- ")
        mul_result = int(mul_1) * int(mul_2)
        print(mul_result)
    elif terminal.upper() == "START DIVISION":
        div_1 = input("Dividend- ")
        div_2 = input("Divisor- ")
        div_result = int(div_1) / int(div_2)
        print(div_result)
    elif terminal == "quit":
        break
    else:
        print("Invalid Command! (Error Code 1)")
