from art import logo
from menu import MENU, resources
import os


def check_choice(ccchoice):
    """Take user choice and return coffee value"""
    if ccchoice == 'espresso':
        return "Your coffee costs $1.50"
    elif ccchoice == 'latte':
        return 'Your coffee costs $2.50'
    elif ccchoice == 'cappuccino':
        return 'Your coffee costs $3.00'
    else:
        return 'Selection not in the menu.'


def check_money(cmchoice):
    """Requests coins, checks if amount is enough and returns change"""
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    money_paid = (quarters*0.25)+(dimes*0.10)+(nickles*0.05)+(pennies*0.01)

    if cmchoice == "espresso" and money_paid >= 1.50:
        change = money_paid - 1.50
        print(f"Your change is: ${change}.")
        return 1.50
    elif cmchoice == "latte" and money_paid >= 2.50:
        change = money_paid - 2.50
        print(f"Your change is: ${change}.")
        return 2.50
    elif cmchoice == "cappuccino" and money_paid > 3.00:
        change = money_paid - 3.00
        print(f"Your change is: ${change}.")
        return 3.00
    else:
        print("Insufficient coins.")


def enough_ingredients(order_ingredients):
    """Returns True when order can be made, False if ingredients are insufficient."""
    for i in order_ingredients:
        if order_ingredients[i] > resources[i]:
            print(f"Sorry there is not enough {i}.")
            return False
    return True


def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")


print(logo)
on = True
money = 0.00
new_resources = resources

while on:

    choice = input("What would you like espresso, latte or cappuccino? ").lower()
    if choice == "off":
        on = False
    elif choice == "report":
        water = new_resources["water"]
        milk = new_resources["milk"]
        coffee = new_resources["coffee"]
        print(f"Water: {water}ml\nMilk: {milk}ml\nCoffee: {coffee}g\nMoney: ${money}")
    else:
        print(check_choice(choice))
        drink = MENU[choice]
        if enough_ingredients(drink["ingredients"]):
            print("Please insert coins.")
            money += check_money(choice)
            make_coffee(choice, drink["ingredients"])



