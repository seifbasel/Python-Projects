from art import art

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 7,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 15,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 20,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100}


def cappuccino():
    if resources["water"] < 250 or resources["milk"] < 100 or resources["coffee"] < 24:
        print("Sorry there is not enough resources")
    elif money < 20:
        print("Sorry there is not enough money")
    else:
        print("here is your cappuccino")
        resources["water"] = resources["water"] - 250
        resources["milk"] = resources["milk"] - 100
        resources["coffee"] = resources["coffee"] - 24
        change = money - 20
        print(f"change is {change}")


def espresso():
    if resources["water"] < 50 or resources["coffee"] < 18:
        print("Sorry there is not enough resources")
    elif money < 7:
        print("Sorry there is not enough money")
    else:
        print("here is your espresso")
        resources["water"] = resources["water"] - 50
        resources["coffee"] = resources["coffee"] - 18
        change = money - 7
        print(f"change is {change}")


def latte():
    if resources["water"] < 200 or resources["milk"] < 150 or resources["coffee"] < 24:
        print("Sorry there is not enough resources")
    elif money < 15:
        print("Sorry there is not enough money")
    else:
        print("here is your latte")
        resources["water"] = resources["water"] - 200
        resources["milk"] = resources["milk"] - 150
        resources["coffee"] = resources["coffee"] - 24
        change = money-15
        print(f"change is {change}")


def report():
    for i in resources:
        print(i)
        print(resources[i])


def choice(choice):
    if choice == "report":
        report()
    elif choice == "espresso":
        espresso()
    elif choice == "latte":
        latte()
    elif choice == "cappuccino":
        cappuccino()


print(art)
enter = True
while enter:
    print("What would you like? (espresso/latte/cappuccino):")
    choice1 = input().lower()
    print("enter the coins. ")
    pounds = int(input("how many pounds: "))
    half_pounds = int(input("many half pounds: "))
    money = half_pounds / 2 + pounds
    choice(choice1)
    if choice1 == "off":
        enter = False