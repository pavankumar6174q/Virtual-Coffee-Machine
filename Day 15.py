MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

profit = 0
def resources_sufficient(order_ingredients):
    """RETURNS WHETHER THE MACHINES HAS ENOUGH RESOURCES TO MAKE THE DRINK OR NOT"""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"sorry we ran out of ingredients ")
            return False
        return True
not_stop = True

def coins():
    """"TAKES THE COINS INPUT AND MULTIPLIES THEM WITH THE RESPECTED VALUES AND ADD IT TO THE TOTAL"""
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total

def payment_calculations(money_received, drink_cost):
    """CALCULATED THE MONEY RECEIVE WITH THE DRINK COST AND RETURNS THE CHANGE"""
    if  money_received >= drink_cost :
        change = round(money_received - drink_cost, 2)
        print(f"Here is your  ${change}")
        global profit
        profit += drink_cost
        return True
    else:
        print("money refunded less amount")
        return False

def make_coffee(drink_name, order_ingredinets):
    """TAKES THE INGREDIENTS OF THE DRINK AND SUBTRACTS THE ITEMS FROM THE MACHINE """
    for items in order_ingredinets:
        resources[items] -= order_ingredinets[items]
    print(f"Here is your {drink_name} ☕️. Enjoy!")



while not_stop:


    user_choice = input("What would you like? (espresso/latte/cappuccino):").lower()
    if user_choice == 'off':
        not_stop = False
    elif user_choice == 'report':
        print(f'Water: {resources["water"]}ml')
        print(f'Milk: {resources["milk"]}ml')
        print(f'Coffee:{resources["coffee"]}g')
        print(f'Money: ${profit}')
    else:
        drink = MENU[user_choice]
        if resources_sufficient(drink["ingredients"]):
            payment = coins()
            payment_calculations(payment, drink["cost"])
            make_coffee(user_choice, drink["ingredients"])











































































