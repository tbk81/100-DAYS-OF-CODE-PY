from menu_file import menu


current_resources = {
    "water": 1000,
    "milk": 500,
    "coffee": 200,
    "money": float(0.00),
}

def pr_report():
    print(f"Water: {current_resources['water']} mL\nMilk: {current_resources['milk']} mL\n"
          f"Coffee: {current_resources['coffee']} g\nMoney: ${current_resources['money']:.2f}")


def check_resources(drink):
    for key in menu[drink]['ingredients']:
        if menu[drink]['ingredients'][key] > current_resources[key]:
            print(f"There is not enough {key}")
            return False
    return True


def coin_op():
    total = float(0)
    quart = float(input("How many quarters: "))
    di = float(input("How many dimes: "))
    nic = float(input("How many nickles: "))
    pen = float(input("How many pennies: "))
    total = quart*.25 + di*.1 + nic*.05 + pen*.01
    return total


def transaction_op(money, drink):
    drink_cost = menu[drink]['cost']
    if money < drink_cost:
        print("Not enough money.")
        return False
    elif money > drink_cost:
        print(f"Here is your change: ${money - drink_cost:.2f}")
        current_resources['money'] += drink_cost
        return True
    else:
        current_resources['money'] += drink_cost
        return True
    

def deduct_resources(drink):
    for key in menu[drink]['ingredients']:
        current_resources[key] -= menu[drink]['ingredients'][key]


machine_on = True
while machine_on:
    usr_choice = input("What would you like? (espresso/latte/cappuccino): ")
    if usr_choice == "off":
        machine_on = False
    elif usr_choice == "report":
        pr_report()
    else:
        if check_resources(usr_choice):
            if transaction_op(coin_op(), usr_choice):
                deduct_resources(usr_choice)
                print(f"Enjoy your {usr_choice}!")
        else:
            machine_on = False
