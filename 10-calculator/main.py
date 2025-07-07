from art import logo

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def calculator():
    print(logo)
    calc_running = True
    num1 = float(input("Type the first number: "))
    while calc_running:
        for key in operations:
            print(key)
        operand = input("Pick an operation: ")
        num2 = float(input("Type the second number: "))
        calculation = operations[operand](num1, num2)
        print(f"{num1} {operand} {num2} = {calculation}")
        usr_choice = input(f"Type 'y' to to continue calculating with {num1}, or type 'n' to start a new "
                           f"calculation: ").lower()
        if usr_choice == "y":
            num1 = calculation
        elif usr_choice == "n":
            calc_running = False
            print("\n" * 20)
            calculator()


calculator()
