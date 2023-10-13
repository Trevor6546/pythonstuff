#Files and Exceptions

#file pi_digits.txt
#3.14159
#26340192
#30491203

#file file_reader.py
with open(pi_digits.txt) as file_object:
    contents = file_object.read()
    print(contents)
#this outputs:
#3.14159
#26340192
#30491203
#
#to get rid of whitespace, change print(contents) to print(contents.rstrip())
#if file isn't in same directionary as python file
with open ('text_files\filename.txt') as file_object

for line in file_object:
    print(line) #prints each line at a time from a file

lines = file_object.readlines()

for line in lines:
    print(line.rstrip())

pi_string = " "
for line in lines:
    pi_string += line.strip()

birthday = input("What is your birthday, in the form ddmmyy: ")
if birthday in pi_string:
    print("You birthday is in pi")
else:
    print("no")

#writing to a file
filename = reuslts.txt

with open(filename, 'w') as file_object:
    file_object.write("babbaboey\n")
    file_object.write("this is a seperate line.\n")

#appending to a file (already has text in it)
filename = test.txt

with open(filename, 'a') as file_object:
    file_object.write("hello\n")

#Exceptions
try:
    print(5/0)
except ZeroDivisionError:
    print("you can't divide by 0")

#try/exception statemnets can be used to prevent a program from crashing / doing impossible operations
def count_words(filename):
    try:
        with open(alice.txt) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        print("File doesn't exist")
        pass #can be used if you want to silently fail, no output message just skipping the try statement
    else:
        words = contents.split() #creates an array with all the words in it
        num_words = len(words)
        print("The file " + filename + " has " + num_words + " in it.")

filename = alice.txt
file2 = swag.txt
count_words(filename)
count_words(file2)

#json
import json
numbers = [2,3,5,7,11,13]

filename = numbers.json
with open(filename, 'w') as f_obj:
    json.dump(numbers, f_obj) #sends it to the json file

#seperate file
import json

filename = numbers.json
with open(filename) as f_obj:
    json.read(numbers)

#sending user input to json
import json

filename = username.json

with open(filename, 'w') as f_obj:
    json.dump(username, f_obj)

import json

filename = username.json
with open(filename) as f_obj:
    username = json.load(f_obj)

#Refactoring
import json

def greet_user():
    filename = user.json
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        username = input("What is your name: ")
        with open(filename, 'w') as f_obj:
            json.dump(username, f_obj)
    else:
        print("Welome back " + username)


