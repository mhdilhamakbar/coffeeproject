
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

income = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def is_resources_enough(order_coffee):
    for item in order_coffee :
        if order_coffee[item] >= resources[item]:
            print(f"There's not enough {item}")
            return False
        return True

def coin():
    print("Pleas Insert Coins: ")
    total = int(input("how many quarters?"))  * 0.25
    total += int(input("how many dimes?")) * 0.1
    total += int(input("how many nickles?")) * 0.05
    total += int(input("how many pennies?")) * 0.01
    return total


def transaction(money_amount, cost_coffee):
    if money_amount >= cost_coffee:
        change = round(money_amount - cost_coffee, 2)
        print(f"Change = {change}")
        global income
        income += cost_coffee
        return True
    else:
        print("Sorry that's not enough money")
        return False

def make_coffe(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print("Hear is your drink")
is_on = True
while is_on:
    order = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if order == "off" :
        is_on = False
    elif order == "report" :
        print(f"water:{resources['water']}ml")
        print(f"milk:{resources['milk']}ml")
        print(f"coffee:{resources['coffee']} ml")
        print(f"money:${income}")
    else :
        drink = MENU[order]
        if is_resources_enough(drink["ingredients"]):
            payment = coin()
            if transaction(payment, drink["cost"]):
                make_coffe(order, drink["ingredients"])







    #     print(MENU)
    #  = ["name"]
    # description = account["description"]
    # country = account["country"]
    # # print(f'{name}: {account["follower_count"]}')
    # return f"{name}, a {description}, from {country}"
    #
