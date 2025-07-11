from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

machine_on = True
while machine_on:
    usr_choice = input(f"What would you like? ({menu.get_items()}): ")
    if usr_choice == "off":
        machine_on = False
    elif usr_choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(usr_choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
