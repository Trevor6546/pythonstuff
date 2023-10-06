#Working with lists
cars = ["honda", "ford", "toyota"]
for car in cars:
    print(car) #prints each element of the index

for car in cars:
    print(car + " is my favorite car") #these print statements work the same as any other one
#indentation matters

for value in range (1,5):
    print(value) #will go 4 times and print {1,2,3,4}

numbers = list(range(1,6))
#1,2,3,4,5

even_numbers = list(range(2,11,2))
#2,4,6,8,10

squares = []
for value in range(1,11):
    square = value**2
    squares.append(square)

#1,4,9,16,25,36,49,64,81,100

digits = [1,4,6,10,16]
min(digits) #1
max(digits) #16
sum(digits) #37

squares = [value**2 for value in range(1,11)]
#1,4,9,16,25,36,49,64,81,100

people = ["John", "Bob", "Tina", "Jill", "Evan"]
print(people[0:3]) #starts at index 0, ends before 3 --> "John", "Bob", "Tina"
print(people[:2]) #automatically starts at 0 --> "John", "Bob"
print(people[3:]) #starts at 3, goes until the end --> "Jill", "Evan"
print(people[-2:]) #prints the last 2 elements no matter the length --> "Jill", "Evan"

presidents = ["Biden", "Trump", "Obama", "Bush", "Clinton"]
for president in presidents[:3]:
    print(president) #will print the first three of the list --> "Biden", "Trump", "Obama"

fav_cities = ["LA", "DC", "Boston"]
friends_fav_cities = fav_cities[:] #copies the list into another variable. The : makes them two seperate
friends_fav_cities = fav_cities #any change made to either one changes the other as well
fav_cities.append("Berlin")
friends_fav_cities.append("Amsterdam")
#can be changed as two seperate entities

#tuple
coordinates = (0,10)
coordinates[0] #0
coordinates[1] #10
coordinates[0] = 20 #ERROR, contents of a tuple can not be changed

for coordinate in coordinates:
    print(coordinate) #0 10

#to change a tuple you need to overwrite it
cooridnates = (50, 100)
#used for when things shouldn't be changed.