from coffee_data import MENU, resources

shop_money = 0


def calculate_money(q1, d1, n1, p1):
    """Calculate total money and return the value"""
    quarters = 0.25
    dimes = 0.10
    nickles = 0.05
    pennies = 0.01

    total_user_money = q1 * quarters + d1 * dimes + n1 * nickles + p1 * pennies

    return total_user_money


def show_report(current_w, current_m, current_c, shop_m):
    """Show the report function"""
    return f"Water: {current_w} \nMilk:  {current_m}\nCoffee: {current_c}\nShop total Money: ${shop_m}"


def espresso(current_w, current_c, ):
    resources["water"] = current_w - MENU["espresso"]["ingredients"]["water"]
    resources["coffee"] = current_c - MENU["espresso"]["ingredients"]["coffee"]

    return resources


def latte(current_w, current_c, current_m):
    resources["water"] = current_w - MENU["latte"]["ingredients"]["water"]
    resources["coffee"] = current_c - MENU["latte"]["ingredients"]["coffee"]
    resources["milk"] = current_m - MENU["latte"]["ingredients"]["milk"]

    return resources


def cappuccino(current_w, current_c, current_m):
    resources["water"] = current_w - MENU["cappuccino"]["ingredients"]["water"]
    resources["coffee"] = current_c - MENU["cappuccino"]["ingredients"]["coffee"]
    resources["milk"] = current_m - MENU["cappuccino"]["ingredients"]["milk"]

    return resources


# final_game = True
# while final_game:
current_water = resources["water"]
current_coffee = resources["coffee"]
current_milk = resources["milk"]

game_on = True

while game_on:

    user_choice = input("What would you like? (espresso/latte/cappuccino): ")

    if user_choice == 'report':
        print(show_report(resources["water"], resources["milk"], resources["coffee"], shop_money))

    elif user_choice == 'off':
        game_on = False

    elif user_choice == 'espresso':
        if current_water >= MENU["espresso"]["ingredients"]["water"] and current_coffee >= \
                MENU["espresso"]["ingredients"]["coffee"]:
            print("Please Insert Coin. ")
            q = float(input("How many quarters?: "))
            d = float(input("How many dimes?: "))
            n = float(input("How many nickles?: "))
            p = float(input("How many pennies?: "))
            user_money = calculate_money(q, d, n, p)
            if user_money >= 1.50:
                user_money = user_money - 1.50
                info = espresso(current_water, current_coffee)
                if user_money > 0:
                    user_money1 = "{:.2f}".format(user_money)
                    print(f"Here is {user_money1} in change.")
                print("Here is your espresso ☕ Enjoy! ")
                shop_money = shop_money + 1.05
                current_water = resources["water"]
                current_coffee = resources["coffee"]
                current_milk = resources["milk"]
            else:
                print("Sorry that's not enough money. Money refunded")

        else:
            if current_water < MENU["espresso"]["ingredients"]["water"]:
                print("Sorry there is not enough Water.")
            elif current_coffee < MENU["espresso"]["ingredients"]["coffee"]:
                print("Sorry there is not enough coffee.")

    elif user_choice == 'latte':
        if current_water >= MENU["latte"]["ingredients"]["water"] and current_coffee >= MENU["latte"]["ingredients"][
            "coffee"] and current_milk >= MENU["latte"]["ingredients"]["milk"]:
            print("Please Insert Coin. ")
            q = float(input("How many quarters?: "))
            d = float(input("How many dimes?: "))
            n = float(input("How many nickles?: "))
            p = float(input("How many pennies?: "))
            user_money = calculate_money(q, d, n, p)
            if user_money >= 2.50:
                user_money = user_money - 2.50
                info = latte(current_water, current_coffee, current_milk)
                if user_money > 0:
                    user_money1 = "{:.2f}".format(user_money)
                    print(f"Here is {user_money1} in change.")
                print("Here is your latte ☕ Enjoy! ")
                shop_money = shop_money + 2.50
                current_water = resources["water"]
                current_coffee = resources["coffee"]
                current_milk = resources["milk"]
            else:
                print("Sorry that's not enough money. Money refunded")
        else:
            if current_water < MENU["latte"]["ingredients"]["water"]:
                print("Sorry there is not enough Water.")
            elif current_coffee < MENU["latte"]["ingredients"]["coffee"]:
                print("Sorry there is not enough coffee.")
            elif current_coffee < MENU["latte"]["ingredients"]["milk"]:
                print("Sorry there is not enough milk.")

    elif user_choice == 'cappuccino':
        if current_water >= MENU["cappuccino"]["ingredients"]["water"] and current_coffee >= \
                MENU["cappuccino"]["ingredients"]["coffee"] and current_milk >= MENU["cappuccino"]["ingredients"][
            "milk"]:
            print("Please Insert Coin. ")
            q = float(input("How many quarters?: "))
            d = float(input("How many dimes?: "))
            n = float(input("How many nickles?: "))
            p = float(input("How many pennies?: "))
            user_money = calculate_money(q, d, n, p)
            if user_money >= 3.00:
                user_money = user_money - 3.00
                info = cappuccino(current_water, current_coffee, current_milk)
                if user_money > 0:
                    user_money1 = "{:.2f}".format(user_money)
                    print(f"Here is {user_money1} in change.")
                print("Here is your cappuccino ☕ Enjoy! ")
                shop_money = shop_money + 3.00
                current_water = resources["water"]
                current_coffee = resources["coffee"]
                current_milk = resources["milk"]
            else:
                print("Sorry that's not enough money. Money refunded")
        else:
            if current_water < MENU["cappuccino"]["ingredients"]["water"]:
                print("Sorry there is not enough Water.")
            elif current_coffee < MENU["cappuccino"]["ingredients"]["coffee"]:
                print("Sorry there is not enough coffee.")
            elif current_coffee < MENU["cappuccino"]["ingredients"]["milk"]:
                print("Sorry there is not enough milk.")
