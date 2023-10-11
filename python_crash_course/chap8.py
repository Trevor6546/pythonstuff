#Functions
def greet_user():
    print("Hello user")

greet_user() #executes function

def greet_user(username):
    print("Hello " + username)

greet_user("tnovak")

def describe_pet(animal_type, pet_name):
    print("\nI have a " + animal_type)
    print("\nIt's name is " + pet_name)

describe_pet("carcal", "gosha") #takes multiple inputs

def describe_pet(animal_type, pet_name = "willie"): #can make default names, so if no variable is specified it will be automatically used.
    print("\nI have a " + animal_type)
    print("\nIt's name is " + pet_name)

def get_formated_name(first_name, last_name):
    full_name = first_name + " " + last_name
    return full_name.title() #return value

dj = get_formated_name("DJ", "khaled")
print(dj)

def get_formated_name(first_name, last_name, middle_name): #opitional arguments
    if middle_name:
        full_name = first_name + " " + middle_name + " " + last_name
    else:
        full_name = first_name + " " + last_name
    return full_name.title() #return value

def greet_users(users): #lists in functions
    for user in users:
        print("Hello " + user)

usernames = ["asdf", "dfggh"]
greet_users(usernames)

#lists can be modified in functions
def print_models(unprinted_designs, completed_models):
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print("Printing Model: " + current_design)
        completed_models.append(current_design)

def showCompletedModels(completed_models):
    print("\n The following models have been completed.")
    for completed_model in completed_models:
        print(completed_model)

completed_models = []
unprinted_designs = ["iphone", "robot", "spaceship"]
print_models(unprinted_designs, completed_models)
showCompletedModels(completed_models)

print_models(unprinted_designs[:], completed_models) #the [:] makes a copy of the list for the function so the original remains unedited

#passing an unknown number of arguments in a function
def makePizza(*toppings): # '*' creates a tuple that all input is put into
    print(toppings)

def makePizzaa(*toppings):
    for topping in toppings:
        print("\n - " + topping)

makePizza("cheese")
makePizza("chesse", "pepproni", "olives")

def build_profile(first, last, **user_info):
    profile = {}
    profile["first_name"] = first
    profile["last_name"] = last
    for key, value in user_info.items(): #takes in additional information
        profile[key] = value
    return profile

user_profile = build_profile('albert', 'einstein', location = 'princeton', field = 'physics')
print(user_profile)

#in a seperate file called pizza.py
def make_pizza(size, *toppings):
    print("\nMaking a " + str(size) + " -inch pizza with the following toppings")
    for topping in toppings:
        print(topping)

#in a seperate file called making_pizzas.py
import pizza #imports the contents of pizza.py
 
pizza.make_pizza(12, "cheese", "pepperoni") #finds the make_pizza function in pizza and calls it

#we can remove the pizza.make_pizza part by doing:
from pizza import make_pizza
make_pizza(16, "cheese")

#we can also change the name of a function or file itself by doing:
import pizza as p
p.make_pizza(10, "nothing")
#or
from pizza import make_pizza as mp
mp(10, "nothing")

#all functions from a program can be imported by saying
from pizza import *

