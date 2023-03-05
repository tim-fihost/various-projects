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
            "water":200,
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
MONEY = 0
def transaction(data,user):
    global MONEY
    if MENU[data]['cost'] == user:
        MONEY += user
        choice(user_answer)
        print("Making Coffe!")
    else:
        print("Error, try again!")
def checking_resources(data):
    for i,k in MENU[data]['ingredients'].items():
        if resources[i] <= k:
            print(f"Sorry there is not enough {i}")
            return False
    return True
def choice(data):
    resources['water'] -= MENU[data]['ingredients']['water']
    if 'milk' in MENU[data]['ingredients']:
        resources["milk"]-=MENU[data]['ingredients']['milk']
    resources["coffee"]-=MENU[data]['ingredients']['coffee']
def report(data,user):
    if data == "report":
        print(f"""
        Water: {resources['water']}
        Milk: {resources['milk']}
        Coffee: {resources['coffee']}
        Money: ${MONEY}
        """
        )
    else:
        if checking_resources(data) == False:
            print("Fill, the means. First!")
        else:
            transaction(data,user)
            print(f"\tWater: {MENU[data]['ingredients']['water']}")
            if 'milk' in MENU[data]['ingredients']:
                print(f"\tMilk: {MENU[data]['ingredients']['milk']}")
            print(f"\tCoffee: {MENU[data]['ingredients']['coffee']}")
            print(f"\tCost: ${MENU[data]['cost']}")
while True:
    user_answer = input("What would woy like (espresso/latte/cappuccino): ")
    if user_answer == "off":
        print("Good Bye!")
        break
    user_insert_money = float(input("Insert Card and type amount: "))
    report(user_answer,user_insert_money)