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
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
def have_enough(ingredients):
    for item in ingredients:
        if ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
        return True
def enough_money(money, cost):
    if money >= cost:
        change = round(money - cost, 2)
        print(f"here is your change ${change}")
        global profit
        profit += cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded")
        return False
def processes_coins():
    print("please insert coins.")
    total = int(input("how meny quarters?: ")) * 0.25
    total += int(input("how meny dimes?: ")) * 0.1
    total += int(input("how meny nickels?: ")) * 0.05
    total += int(input("how meny pennies?: ")) * 0.01
    return total
def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -=order_ingredients[item]
    print(f"here is your {drink_name}")



is_on = True
while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water:{resources['water']} ")
        print(f"Milk: {resources['milk']}")
        print(f"Coffee: {resources['coffee']}")
        print(f"Money: {profit}")
    elif choice == "menu":
        print(f"espresso {MENU['espresso']['cost']}")
        print(f"latte {MENU['latte']['cost']}")
        print(f"cappuccino {MENU['cappuccino']['cost']}")
    else:
        drink = MENU[choice]
        if have_enough(drink["ingredients"]):
            pyment = processes_coins()
            if enough_money(pyment,drink['cost']):
                make_coffee(choice, drink['ingredients'])

