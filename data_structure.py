"""list = []  # create list
for num in range(1,11):  # add value to list
    # list += [num]
print(num)
# Access list value by iteration
for item in list:
    print(item)

list = []
for item in range(1,11):
    # list += [item]
    # print(item)  # To print in horizontal style
    print(list)  # To print in trianguler style

# Access list value by iteration
for item in list:
    print(item)

for i in range(len(list)):
    print(i,list[i])

h = int(input('Enter hours'))
m = int(input('Enter minutes'))
s = int(input('Enter second'))
current_time = (h,m,s)
print('value of current time is',current_time)

# Unpacking sequence
string = 'abc'
list = ['a',1,78]
tuple = ('a',12)
first, second, third = string
print('Unpacking string', first, second, third)
first, second, third = list
print('Unpacking list',first, second, third)
first, second = tuple
print('Unpacking tuple',first, second)
dict = {}
print('Value of empty dictionary',dict)
grade = {'john':12,'steav':23,'laura':45,'edwin':54}
print('\n print all grade :',grade)
# Access and modify technique
print('\n steav cuurent grade',grade['steav'])
grade['steav'] = 90
print('steav grade after modify',grade['steav'])

# Appending item to list
playlist = []
print('Enter you five fovourate food name')
for i in range(5):
    playname = input('Enter food ')
    playlist.append(playname)
print('\n subscript           value')
for i in range(len(playlist)):
    print(i+1, playlist[i] = {}

dict = {a:b}
item = { inside the elements of dictionary a:b }
key = {a}
value = { crosspandance of b}
month = {1:'january', 2:'february', 3:'march', 4:'april', 5:'may', 6:'june', 7:'july', 8:'august', 9:'september',10:'october',11:'november',12:'december'}
print('Dictionary are:',month.items())
print('the dictionary keys are:',month.keys())
print('value are:',month.values())
for key in month.keys():
    print([key] , month[key])

num_lst = []
for i in range(1, 11):
    num_lst.append(i)
print('original list is', i)
for index, i in enumerate(num_lst):
    if i %2 == 0:
        del num_lst[index]
print(num_lst)

Topper = (('Rahul', 'bsc', 92.0), ('joti', 'btech', 89.8), ('rakesh', 'bca', 87.5))
for i in Topper:
    print(i)
choice = input('Do you want to edit the name')
if choice == 'y':
    name = input('Please enter the name:')
    new_name = input('Enter the correct name:')
    new_course = input('Enter the new course:')
    new_aggr = input("Enter the new aggregate:")
    i = 0
    new_topper = ()
    while i< len(Topper):
        if Topper[i][0] == name:
            new_topper += (new_name, new_course, new_aggr)
        else:
            new_topper += Topper[i]
            i+= 1

for i in new_topper:
    print(i)

print("Enter -1 to exit")
circumference = ()
while True:
    r = float(input('Enter radius'))
    if r == -1:
        break
    else:
        dict = {r:2*3.14*r}
        circumference.update(dict)
print(circumference)

m_cm = {x: x*100 for x in range(1,11)}
print(m_cm)"""

dict = {x: x**3 for x in range(10) if x%2==1}
print(dict)


