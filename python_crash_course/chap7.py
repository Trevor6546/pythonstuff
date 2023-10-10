#User Input and While Loops
message = input("What do you want to say: ")
print("You said: " + message)

age = input("How old are you?")
#age will be returned as a string and not an int
age = int(age) #turns the input into an int value

#while loops
num = 1
while(num < 5):
    print(num)
    num += 1

#how to kill a while loop
prompt = input("\nTell me something and I will repeat it back: ")
prompt += ("\n Enter quit to end the program")
message = input(prompt)

while(message != "quit"):
    print(message)

#flags

prompt = input("\nTell me something and I will repeat it back: ")
prompt += ("\n Enter quit to end the program")

active = True
while active:
    message = input(prompt)

    if message == "quit":
        active = False #active serves as a flag for the program
    else:
        print(message)

#break

while True:
    if message == "quit":
        break #if break is executed, the loop will terminate
    else:
        print(message)

#continue
while True:
    if message == "quit":
        continue #will just skip this iteration of the loop
    else:
        print(message)

#using while loops to move from one list to another
unconfirmed_users = ["josh", "jess", "jose"]
confirmed_users = []

while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    confirmed_users.append(current_user)

#removing all instances of something in a list
pets = ["dog", "cat","fish","turtle"]
while "cat" in pets:
    pets.remove("cat")

#using input to fill a dictionary

responses = {}

polling_active = True #flag

while polling_active:
    name = input("Whats your name")
    response = input("Who are you voting for")

    responses[name] = response

    repeat = input("Would you like another person to respond (Yes/No)")

    if repeat == "No":
        polling_active = False

for name, response in responses.items():
    print(name + " is voting for: " + response)

