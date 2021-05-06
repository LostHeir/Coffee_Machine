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
    "money": 0,
}

turn_off = False


def report():
    """Prints how much resources are in machine."""

    print(f"Water: {resources['water']}")
    print(f"Milk: {resources['milk']}")
    print(f"Coffee: {resources['coffee']}")
    print(f"Money: {resources['money']}")
    input("Type 'ok' to continue: ")


def check_resources(coffee):
    """Checks if there is enough resources in machine."""
    for item in MENU[coffee]['ingredients']:
        is_enough = resources[item] - MENU[coffee]['ingredients'][item]
        if is_enough < 0:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def use_resources(coffee):
    """"Uses resources in machine"""
    global resources
    for item in MENU[coffee]['ingredients']:
        resources[item] -= MENU[coffee]['ingredients'][item]


def make_coffee(coffee):
    """"Main logic responsible for making a coffee"""
    if check_resources(coffee):
        quarters = int(input("How many quarters?: ")) * 0.25
        dimes = int(input("How many dimes?: ")) * 0.1
        nickles = int(input("How many nickles?: ")) * 0.05
        pennies = int(input("How many pennies?: ")) * 0.01
        user_money = round(quarters + dimes + nickles + pennies, 2)

        if user_money == MENU[coffee]["cost"]:
            print(f"Here is your {coffee}: ☕")
        elif user_money > MENU[coffee]["cost"]:
            change = user_money - MENU[coffee]["cost"]
            use_resources(coffee)
            print(f"Here is ${change} in change.")
            print(f"Here is your {coffee}: ☕")


while not turn_off:
    user_input = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if user_input == "end":
        turn_off = True
        print("Shutting down for maintenance...")
    elif user_input == "report":
        report()
    elif user_input == "espresso":
        make_coffee("espresso")
    elif user_input == "latte":
        make_coffee("latte")
    elif user_input == "cappuccino":
        make_coffee("cappuccino")
    else:
        print("Sorry we don't have it in our Menu..")