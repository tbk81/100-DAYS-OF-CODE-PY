from menu_file import menu

# print(menu)
# print(menu["espresso"]['ingredients']['water'])
# print(menu["espresso"]['cost'])

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
    return True


machine_on = True
while machine_on:
    usr_choice = input("What would you like? (espresso/latte/cappuccino): ")
    if usr_choice == "off":
        machine_on = False
    elif usr_choice == "report":
        pr_report()
    else:
        if check_resources(usr_choice):
            print("hello")
        else:
            machine_on = False

