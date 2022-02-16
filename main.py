import money_machine
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

flag = False
cm = CoffeeMaker()
mn = Menu()
mm = MoneyMachine()

while not flag:
    options = mn.get_items()
    choice = input(f"what you want from {options} ? ")

    if choice == "report":
        cm.report()
        mm.report()
    elif choice == "off":
        flag = True
    else:
        get_drink = mn.find_drink(choice)
        if cm.is_resource_sufficient(get_drink) and (mm.make_payment(get_drink.cost)):
            cm.make_coffee(get_drink)
