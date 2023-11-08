MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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

power = True

totalmoney = 0

def print_report():
    for key in resources:
        print(f"{key}: {resources[key]} units")
    print(f"Total amount of money in this machine: ${totalmoney}")

def check(coffee):
    global resources
    if MENU[coffee]["ingredients"]["water"] >= resources["water"]:
        print("Sorry there is not enough water")
        return False
    if MENU[coffee]["ingredients"]["milk"] >= resources["milk"]:
        print("Sorry there is not enough milk")
        return False
    if MENU[coffee]["ingredients"]["coffee"] >= resources["coffee"]:
        print("Sorry there is not enough coffee")
        return False
    return True

def coinInput():
    coinin = 0
    Qpaid = (0.25 * float(input("How many quarters do you have?\t")))
    Dpaid = (0.1 * float(input("How many dimes do you have?\t")))
    Npaid = (0.05 * float(input("How many nickles do you have?\t")))
    Ppaid = (0.01 * float(input("How many pennies do you have?\t")))
    coinin = Qpaid + Dpaid + Npaid + Ppaid
    return coinin

def rm_resources(coffee):
    global resources
    resources["water"] -= MENU[coffee]["ingredients"]["water"]
    resources["milk"] -= MENU[coffee]["ingredients"]["milk"]
    resources["coffee"] -= MENU[coffee]["ingredients"]["coffee"]

while power == True:
    coffee = input("What would you like? (espresso/latte/cappuccino):\t")
    if coffee == "off":
        power = False
    elif coffee == "report":
        print_report()
    elif coffee == "espresso" or coffee == "latte" or coffee == "cappuccino":
        if check(coffee):
            paid = coinInput()
            if paid > MENU[coffee]["cost"]:
                moneyin = MENU[coffee]["cost"]
                totalmoney += moneyin
                refund = round((paid - moneyin), 2)
                rm_resources(coffee)
                print(f"Thank you for the ${MENU[coffee]['cost']}. Here is your coffee and your change of ${refund}")
            else:
                print("Sorry not enough money. Money refunded")
    else:
        print("Invalid entry. Please try again")
