#If Statements
cars = ["audi", "bmw", "toyota", "subaru"]
for car in cars:
    if car == "bmw":
        print(car.upper())
    else:
        print(car.title())

topping = "pepperoni"
if topping != "pineapple":
    print("No pineapple!")

requested_toppings = ["pepperoni", "olives", "bacon"]

if "pepperoni" in requested_toppings:
    print("Yippee") #will print
if "pineapple" in requested_toppings:
    print("Yippee") # will not print

banned_users = ["andrew", "carolina", "david"]
user = "marie"
if user not in banned_users:
    print(user.title() + " , you can post a response if you wish.")

game_active = True
banned = False

age = 17
if age >= 18:
    print("you can vote")
else: #if the if isn't satisifed it goes to the else
    print("you can't vote")

age = 12
if age < 4:
    print("your cost is $4")
elif age < 18:
    print("your cost is $5")
else:
    print("your cost is $10")

requested_toppings = ["pepperoni", "extra cheese"]
if "pepperoni" in requested_toppings:
    print("adding pepperoni")
elif "mushrooms" in requested_toppings:
    print("adding musshrooms")
elif "extra cheese" in requested_toppings:
    print("adding extra cheese")

for requested_topping in requested_toppings: #outputs each element in list
    print("Adding " + requested_topping)

print("\n Your pizza is finished")

cars = ["honda", "subaru", "ford", "toyota"]
for car in cars:
    if car == "honda":
        print("no more hondas")
    else:
        print("you picked " + car)

requested_toppings = []
if requested_toppings:
    for topping in requested_toppings:
        print(topping)
else:
    print("no pizza toppings")

aviliable_toppings = ["pepperoni", "cheese", "olives", "green peppers", "sausage"]
requested_toppings = ["mushrooms", "cheese", "olives"]

for requested_topping in requested_toppings:
    if requested_topping in aviliable_toppings:
        print("Adding " + requested_topping + " to pizza.")
    else:
        print("Not in stock")
print("\nFinished making your pizza.")