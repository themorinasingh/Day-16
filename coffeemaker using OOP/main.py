from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from prettytable import PrettyTable

#setting up local menu and payment system

payment_system = MoneyMachine()
my_menu = Menu()

#can we make a drink, setting up coffee maker
my_coffeemaker = CoffeeMaker()

coffee_maker_is_on = True

while coffee_maker_is_on:
    order = input("What would you have? latte, espresso, cappuccino: ").lower()


    if order == "off":
        break
    elif order == "report":
        report = PrettyTable()
        report.add_column("Items",["Water", "Milk", "Coffee", "Profit"])
        report.add_column("Value", [my_coffeemaker.resources["water"], my_coffeemaker.resources["milk"], my_coffeemaker.resources["coffee"], payment_system.profit ])
        print(report)
        continue

    chosen_item = my_menu.find_drink(order)

    if not chosen_item :
        print("Order an item in the list above")
        continue

    #handling transaction
    transaction_clear = payment_system.make_payment(chosen_item.cost)

    if transaction_clear:
        if my_coffeemaker.is_resource_sufficient(chosen_item):
            my_coffeemaker.make_coffee(chosen_item)