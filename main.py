from coffee_data import MENU, resources


def calculate_money(q, d, n, p):
    """Calculate total money and return the value"""
    quarters = 0.25
    dimes = 0.10
    nickles = 0.05
    pennies = 0.01

    total_user_money = q * quarters + d * dimes + n * nickles + p * pennies

    return total_user_money


def show_report():
    """Show the report function"""
    return f"Water: {resources['water']} \nMilk:  {resources['milk']}\nCoffee: {resources['coffee']}"


def espresso(current_water, current_coffee, ):
    resources["water"] = current_water - MENU["espresso"]["ingredients"]["water"]
    resources["coffee"] = current_coffee - MENU["espresso"]["ingredients"]["coffee"]

    return resources


def latte(current_water, current_coffee, current_milk):
    resources["water"] = current_water - MENU["latte"]["ingredients"]["water"]
    resources["coffee"] = current_coffee - MENU["latte"]["ingredients"]["coffee"]
    resources["milk"] = current_milk - MENU["latte"]["ingredients"]["milk"]

    return resources


def cappuccino(current_water, current_coffee, current_milk):
    resources["water"] = current_water - MENU["cappuccino"]["ingredients"]["water"]
    resources["coffee"] = current_coffee - MENU["cappuccino"]["ingredients"]["coffee"]
    resources["milk"] = current_milk - MENU["cappuccino"]["ingredients"]["milk"]

    return resources


game_on = True

while game_on:

    user_choice = input("What would you like? (espresso/latte/cappuccino): ")

    current_water = resources["water"]
    current_coffee = resources["coffee"]
    current_milk = resources["milk"]

    if user_choice == 'report':
        show_report()
    elif user_choice == 'espresso':
        print("Please Insert Coin: ")
        q = float(input("How many quarters?: "))
        d = float(input("How many dimes?: "))
        n = float(input("How many nickles?: "))
        p = float(input("How many pennies?: "))
        user_money = calculate_money(q, d, n, p)
        if user_money >= 1.50:
            info = espresso(current_water, current_coffee)
            print(info)
