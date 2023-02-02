"""print('hello world')
print("welcome to \n python")  # Break the line
print('what python can \\ do') # single space will appear
print('i love \a python')  # Alert the system bell
print('python is highly \' versatile')  #Single quote
print('python is more advanced \" tha java')  # Double quote
print('python is more advanced \r tha java but not c++') # Carriage return
print('python is more advanced \b tha java but not c++') # Backspace
print('python is more advanced \t tha java as well not c++' # horizontal tab


variables and names
cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_drivers = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

print("There are", cars, " cars available")
print("Ther are only", drivers, "drivers avaliable")
print("There will be", cars_not_drivers, "empty cars today")
print("We have transport", carpool_capacity, "people today" )
print("We have", passengers, "to carpool today")
print("we need to put about", average_passengers_per_car, "in each cars")


# More variables
my_name = 'tyson xwort'
my_age = 24
my_height = 5.4
my_weight = 51
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'

print(f"Let's talk about {my_name}")
print(f"he is {my_height} inches tall")
print(f"he is my {my_weight} kg heavy")
print(f"Actually that not too little")
print(f"he is got {my_eyes} eyes and {my_hair} hair")
print(f"he teeth is usually {my_teeth} depending on brushing")
total = my_age + my_height + my_weight
print(f"If I add {my_age}, {my_height}, and {my_weight} I get {total}")
print("let's talk about", my_name)

# string and text
types_of_people = 10
x = f"There are {types_of_people} types of people"
binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}"
print(x)
print(y)

print(f"I said: {x}")
print(f"I also said: '{y}'")
halaroius = False
joke_evaluation = "Isn't that joke so funny! {}"
print(joke_evaluation.format(halaroius))
w = "This is tje left side of..."
e = "a string dwith right side."
print(w+e)

# printing printing
formatter = "{} {} {} {}"
print(formatter.format(1, 2, 3, 4))
print(formatter.format('one', 'two', 'three', 'four'))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
    "try your",
    "own text here",
    "maybe a poem",
    "on a song about"
))

# printing printing printing

# Asking questions
print('How old are you', end ='')
age = input()
print('How tall you are', end = '')
height = input()
print('How much do you weight', end = '')
weight = input()
print(f"So, you are {age} old, {height} tall and {weight} heavy")

age = int(input('Enter your age'))

# Unoacking
from sys import argv
script, first, second, third = argv
print("The script is called", script)
print("Your first variable is", first)
print("Youe second variable is", second)
print("Your third variable is", third)"""


