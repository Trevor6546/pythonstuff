#Dictionaries
alien_0 = {"color" : "green", "points" : 5}
print(alien_0["color"]) #"green"
print(alien_0["points"]) #5
newPoints = alien_0["points"]
print("You earned " + newPoints + " points!")

alien_0["x_position"] = 0
alien_0["y_position"] = 25

alien_1 = {}
alien_1["color"] = "grey" #adds to alien_1

alien_2 = {"x_position" : 0, "y_position" : 0, "speed" : "medium"}
print("Original x_position: " + str(alien_2["x_position"]))
if alien_2["speed"] == "slow":
    x_increment = 1
elif alien_2["speed"] == "medium":
    x_increment = 2
else:
    x_increment = 3
alien_2["x_position"] = alien_2["x_position"] + x_increment

del alien_2["speed"] #will remove the speed from the dictionary

#neater way to format a dictionary
favorite_cars = {
    "trevor" : "corvette",
    "john" : "lambo",
    "jess" : "g-wagon"
}

#looping through a dictionary
for key, value in favorite_cars.items():
    print("\nName: " + key)
    print(" Favorite car: " + value) #if items isn't specified it will only get keys

for names in favorite_cars:
    print("\n Name: " + names)

#how to get values
for name in favorite_cars:
    print(name + "'s favorite car is: " + favorite_cars[name])

#when looping through a dictionary, you will get results in random orders.
#to sort a dictionary (get results in alphabetical order) do this:
for name in sorted(favorite_cars):
    print("Hello, " + name)

#another way of just getting the values
for value in favorite_cars.values():
    print(value)

#.keys() will give only keys, .values() will give only values, and .items() will give both

#to handle duplicates in a list
for name in set(favorite_cars.keys()):
    print(name) #won't print any duplicates in the list

#A list of dictionaries

aliens = [alien_0, alien_1, alien_2]

#new list
alien = []

#make 30 new aliens
for alien_number in range(30):
    new_alien = {"color" : "green", "points" : 10}
    aliens.append(new_alien)

#show the first 5 aliens
for x in alien[:5]:
    print(x)

#show how much aliens have been created
print("Total number of aliens: " + str(len(alien)))

#A List in a dictionary

pizza = {
    "crust" : "thick",
    "toppings" : ["pepperoni", "cheese", "bacon"]
}
#summarize the order
print("You ordered a " + pizza["crust"] + "-crusted pizza.")
print("\n Your toppings are: ")
for topping in pizza["toppings"]:
    print(topping)

#dictionary in an dictionary
users = {
    "einstein" : {
        "name" : "Einstein",
        "study" : "physics",
        "location" : "princeton"
    },
    "curie" : {
        "name" : "Curie",
        "study" : "radition",
        "location" : "paris"
    }
}
for username, user_info in users.items():
    print("\nUsername: " + username)
    print("Last Name: " + user_info["name"])