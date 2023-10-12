#Classes
class Dog():

    def __init__(self, name, age): #self is required as the first parameter. It effectively acts as the name of the class for the code within it.
        self.name = name
        self.age = age

    def sit(self):
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        print(self.name.title() + " rolled over.")

my_dog = Dog("willie", 6)
print("My dog's name is " + my_dog.name.title()) #gets the name from object my_dog
print("My dog is " + str(my_dog.age) + " years old")
my_dog.sit()
my_dog.roll_over() #calls the functions

class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0 #can have default values

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
    
    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles driven.")

    def update_odometer(self, mileage):
        self.odometer_reading = mileage

    def increment_odometer(self, increase):
        self.odometer_reading += increase
    
my_car = Car('ford', 'bronco', 1993)
print(my_car.get_descriptive_name())
#my_car.read_odometer = 23,000 #can edit value
my_car.update_odometer(23000)
my_car.increment_odometer(1000)
my_car.read_odometer()

#making children classes
class ElectricCar(Car):
    def __init__(self,make,model,year):
        super().__init__(make,model,year)
        self.battery_size = Battery()


    def describe_battery(self):
        print("The battery used can hold " + self.battery_size + " volts")
my_tesla = ElectricCar('tesla', 'model s', 2022)
print(my_tesla.get_descriptive_name()) #can access methods in the parent class
#If the parent and child have the same function name, the child function will take priority

class Battery():
    def __init__(self, battery_power=70):
        self.battery_power = battery_power

    def get_range(self):
        if self.battery_power == 70:
            range = 240
        elif self.battery_power == 85:
            range = 270

        message = "The car can go about " + range + " miles on a full charge"
        return(message)
    
    def describe_battery(self):
        print("The battery can hold " + self.battery_power + " volts of electricity.")

my_tesla.battery_size.describe_battery() #the battery can hold 70 volts of electricity
my_tesla.battery_size.get_range() #the car can go about 240 miles on a full charge

#classes can be imported from other files
#hypothetical second file (first is called car.py)

from car import Car

my_new_car = Car("audi", "r8", 2023)
print(my_new_car.get_descriptive_name())
my_new_car.odometer_reading = 23000
my_new_car.read_odometer()

#child classes can be imported too
from car import ElectricCar

#to import multiple classes
from car import Car, ElectricCar

#or you can import the whole module
import car

#or import all classes from a module
from module_name import *

#you can also import things from the python library