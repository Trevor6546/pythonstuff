#Lists
bicycles = ["trek", "giant", "yt"]
print(bicycles) #["trek", "giant", "yt"]
print(bicycles[0]) #trek
print(bicycles[-1]) #yt (an index of -1 gives the last element in the list)
message = "My bike is a " + bicycles[0].title() + "."
print(message) #My bike is a Trek.
bicycles[0] = "sondor" #replaces trek with sondor
bicycles.append("trek") #adds trek as the fourth element in the list
bicycles.insert(0, "cannondale") #inserts cannondale at element index 0 without remove what is currently there.
del bicycles[0] #deletes the element at index 0
my_bike = bicycles.pop() #removes the element in the last index and stores it to a variable
friends_bike = bicycles.pop(2) #removes the element at specified index and stores it to a variable.
bicycles.remove('giant') #finds giant in the list and removes it
expensive = "yt"
bicycles.remove(expensive) #removes variable from list
print("I sold my " + expensive.title() + " because it cost too much") #variable can still be used even if removed from list

cars = ["honda", "ford", "tesla", "toyota", "subaru"]
cars.sort() #sorts the cars in alphabetical order
#"ford", "honda", "tesla", "toyota", "subaru"
cars.sort(reverse=True) #sorts the cars in reverse alphabetical order
#"subaru", "toyota", "tesla", "honda", "ford"
print(cars.sorted()) #will sort the list just for the instance it is used. The actual list is not altered.
cars.reverse() #reverses the current order of the list
len(cars) #gives the number of items in the list
#errors
print(cars[100]) #there is no index for cars at 100 so an error will be thrown
dogs = []
print(dogs[-1]) #there is no last element so an error will be thrown
