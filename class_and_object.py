# simple definition of time class
# Time abstract data type
"""class Time:
    def __init__(seimelf):
        # initialization h,m,s to 0
        self.h = 0
        self.m = 0
        self.s = 0
    def printmilitary(self):
        print(self.h, self.m, self.s)
    def printstandered(self):
        stadaredtime = ''
        if self.h == 0 or self.h == 12:
           stadaredtime += '12:'
        else:
            stadaredtime += (self.h%12)
        stadaredtime += (self.m + self.s)
        if self.h < 12:
            stadaredtime += 'AM'
        else:
            stadaredtime += 'PM'
        print(stadaredtime,)

class PrivateClass:
    def __init__(self):
        self.publicData = 'public'
        self.__Private = 'Private'

class Time:
    def __init__(self, hour = 0, minutes = 0, second = 0):
        self.setTime(hour, minutes, second)
    def setTime (self, hour, minutes, second):
        self.setHour = (hour)
        self.setMinutes = (minutes)
        self.setSecond(second)

    def setHour(self,hour):
        if 0<= hour <24:
            self.__hour = hour

    def setMinutes(self, minutes):
        if 0<= minutes < 60:
            self.__minutes = minutes
        else:
            raise ValueError ('Minutes is invalide')
    def setSecond(self, second):
        if 0<= second < 60:
            self.__second = second
        else:
            raise ValueError ('Invalide second')

    def getHour(self):
        return self.__hour
    def getMinutes(self):
        return self.__minutes
    def getSecond(self):
        return self.__second

    def Printstandard(self):
        standardTime = ""
        if self.__hour == 0 or self.__hour == 12:
            standardTime += '12'
        else:
            standardTime += (self.__hour % 12)
        standardTime +=  (self.__minutes, self.__second)
        if self.__hour < 12:
            standardTime += 'AM'
        else:
            standardTime += 'PM'
        print(standardTime)


class car1:
    def __init__(self, color, price):
        self.color = color
        self.price = price

    def show_data(self):
        print('Color is first car is:', self.color)
        print('Price of first car is:', self.price)
class car2:
    def __init__(self, color, price):
        self.color = color
        self.price = price
    def show_data(self):
        print('Color is second car is:', self.color)
        print('Price of second car is:', self.price)


c1 = car1('blue', 5000000)
c2 = car2('red', 70000000)
c1.show_data()
c2.show_data()

class collage:
    def set_data(self, title, depat):
        collage.title = input('Enter title of collage')
        collage.depat = input('Enter the department')
    def get_data(self):
        return collage.title
    def get_data(self):
        return collage.depat


c = collage()
c.set_data('title','depat')
c.get_data()
print("name of the collage is",collage.title)
print('Department os the collage is',collage.depat)

# Question 5 did'nt solve

class Triangle():
    def set_area(self, len, bre, hei):
        Triangle.len = len
        Triangle.bre = bre
        Triangle.hei = hei
    def show_area(self):
        print('Length of triangle',Triangle.len)
        print("Breath of triangle",Triangle.bre)
        print('Heigh of triangle',Triangle.hei)
    def cal_area(self):
        return 1/2*Triangle.len*Triangle.bre*Triangle.hei
t = Triangle()
t.set_area(12, 4, 7)
t.show_area()
t.cal_area()
print('Area of triangle is:',1/2*12*4*7)
class Book:
    def __init__(self,title, author, publisher, isbn):
        self.title = title
        self.author = author
        self.publisher = publisher
        self.isbn = isbn

import mysql.connector
cnx = mysql.connector.connect(user='tyson', password = 'password', host = '127.0.0.1', database = 'employees')
cnx.close()

class student:
    def __init__(self, name):
        self.name = name
        self.marks = []
    def get_data(self):
        for i in range(3):
            m = int(input('Enter marks of student'))
            self.marks.append(m)

    def display_sem1(self):
        print(self.name, 'got',self.marks,'in sem 1')

    def display_sem2(self):
        print(self.name, 'got', self.marks, 'in sem 2')
s1 = student('Tyson')
s1.get_data()
s2 = student('Prem')
s2.get_data()
s1.display_sem1()
s2.display_sem2()

class store:
    __item = []
    __price = []
    def get_data(self):
        for i in range(3):
            it = int(input('Enter item'))
            pr = int(input('Enter price'))
            self.__item.append(it)
            self.__item.append(pr)
    def display(self):
        print('Item code \t Item price')
        for i in range(3):
            print(self.__item[i],'\t\t',self.__price)
    def cal_bill(self, quant):
        total = 0
        for i in range(3):
            total = total + self.__price[i]*quant[i]
        print("----------BILL----------")
        print('ITEM \t PRICE \t QUANTITY \t SUBTOTAL')
        for i in range(3):
            print(self.__item[i],'\t',self.__price[i],'\t',quant[i],'\t',quant[i]*quant[i]*self.__price[i])
            print('*******************************')
            print('Total:',total)


s = store()
s.get_data()
s.display()
q = []
print('Enter the quantity of item:')
for i in range(3):
    q.append(int(input()))
s.cal_bill(q)


class Number:
    def __init__(self):
        self.value = []
    def find_max(self):
        max = " "
        for i in self.value:
            if i > max:
                max = i
        print(max)
    def insert(self):
        value = input('Enter value')
        self.value.append(value)
n = Number()
ch = 'y'
while(ch == 'y'):
    n.insert()
    ch = input('Enter elements if you wish')
n.find_max()

class Book:
    def __init__(self):
        self.author = ''
        self.title = ''
        self.price = 0

    def read(self):
        self.author = input('Enter author of the book')
        self.title = input('Enter title of the book')
        self.price = int(input('Enter the price of the book'))

    def display(self):
        print('Title : ',self.author)
        print('Title',self.title)
        print('Price',self.price)

my_book = []
ch = 'y'
while(ch == 'y'):
    print('''1. Add book
             2. Display book''')
    choice = int(input('Enter choice:'))
    if (choice == 1):
        book = Book()
        book.read()
        my_book.append(book)
    elif(choice ==2):
        for i in my_book:
            i.display()
    else:
        print('Invalide choice')
    ch == input('Do you want tot continue...')
    print('bye!')

b = Book()
b.read()
b.display()

# swap two number using class
class Swap:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        print('Before swaping')
        print('X', self.x)
        print("Y", self.y)

    def swap(self):
        self.x, self.y = self.y, self.x
    def disp(self):
        print('After swaping')
        print('X', self.x)
        print("Y", self.y)
s = Swap(12, 36)
s.swap()
s.disp()

class Time:
    def __init(self, hrs, min, sec):
        self.hrs = 12
        self.min = 60
        self.sec = 60
    def entertime(self,h,m,s):
        h = int(input('Enter hours'))
        m = int(input('Enter minutes'))
        s = int(input('Enter second'))

    def lefttime(self,h,m,s):
        print(h-self.hrs)
t = Time()
t.entertime(h,m,s)
t.lefttime()"""


class X:
    var = 10
    def display(self):
        print('Value of x is :', var)
x = X()
x.display()


