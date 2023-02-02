class X:
    var = 10
    def display(self):
        print('In class method....')
x = X()
print(x.var)
x.display()

class X:
    def __init__(self, val):
        print("In class method...")
        self.val = val
        print("The vlaue of value is ", val)
v = X(10)   # There is no need to call the function, because constructr autommically called

class X():
    def __init__(self, val1, val2):
        self.val1 = val1
        self.__val2 = val2
    def display(self):
        print("From class method val 1 is :", self.val1)
        print("From class method val 1 is :", self.__val2)
x = X(12, 45)
x.display()
print(x.val1)

class Student:
    def __init__(self, name):
        self.name = name
        self.marks = []
     def entermarks(self):
         for i in range(3):
             m =  int(input("Enter marks of student :"))
            self.marks.append(m)
     def display(self):
        print("Marks of student is", self.marks)
s1 = Student('Tyson')
s1.entermarks()
s1.display()
s2 = Student('Prem')
s2.entermarks()
s2.display()

class Employee:
    def __init__(self, name , deg, sal):
        self.name = name
        self.deg = deg
        self.sal = sal
    def display(self):
        print('Name of the person is ', self.name)
        print('Degination of the person is ', self.deg)
        print('Salary of the person is ', self.sal)
e1 = Employee('Tyson', 'manager', 5000)
e1.display()
e2 = Employee('Khurshid', 'ceo', 60000)
e2.display()

import datetime
class Person():
    def __init__(self, name, dob):
        self.name = name
        self.dob = dob
    def check(self):
        today = datetime.date.today()
        age = today.year - self.dob.year
        if today < datetime.date(today.year, self.dob.month, self.dob.day):
            age += 1
        if age>=18:
            print(self.name, 'you are eliga;e for vote')
        else:
            print('You are little')

p = Person('Tyson', datetime.date(1999, 12, 4))
p.check()

import math
class Circle:
    PI = 3.14
    def __init__(self, rad):
        self.rad = rad

    def cal_area(self):
        return Circle.PI*self.rad*self.rad

    def display(self):
        print("area of circle is",Circle.PI*self.rad*self.rad )

c = Circle(7.5)
c.cal_area()
c.display()

class Student:
    __marks = []
    def set_data(self, n, r, m1, m2, m3):
        self.__rollno = r
        self.__name = n
        self.__marks.append(m1)
        self.__marks.append(m2)
        self.__marks.append(m3)
    def display(self):
        print("Student details")
        print('Roll no of the student is :', self.__rollno)
        print("NAme jof the student is :", self.__name)
        print("Marks of student is :", self.total())
    def total(self):
        m = self.__marks
        return m[0] + m[1]+ m[2]

r = int(input("Enter roll number jof student :"))
n = input("Enter name of the student is :")
m1 = int(input("Enter marks of first subjext :"))
m2 = int(input("Enter marks of second subjext :"))
m3 = int(input("Enter marks of third subjext :"))

s = Student()
s.set_data(r, n, m1, m2, m3)
s.display()

class Rectange:
    def get_area(self):
        self.__l = int(input('Enter length :'))
        self.__b = int(input('Enter breadt :'))

    def show_data(self):
        print("Length of Rectangle is :", self.__l)
        print("Breadth  of rectangle is :", self.__b)

    def cal_area(self):
        return self.__l * self.__b

r = Rectange()
r.get_area()
r.show_data()
print('Area of Rectangle is :', r.cal_area())
# print(r.__l)   private data member con not call out of the class


class Fraction:
    def get_data(self):
        self.__num = int(input('Enter num :'))
        self.__deno = int(input('Enter deno :'))
        if self.__deno == 0:
            print("Fraction is not possible")
            exit()
    def display(self):
        self.__simplify()
        print(self.__num / self.__deno)

    def __simplify(self):
        print("Simplified fraction is :")
        common_divisior = self.__GCD(self.__num, self.__deno)
        self.__num = self.__num / common_divisior
        self.__deno = self.__deno / common_divisior

    def __GCD(self, a, b):
        if b == 0:
            return a
        else:
            return b
f = Fraction()
f.get_data()
f.display() 

class Number:
    even = 0
    def check(self, num):
        if num % 2 ==0:
            self.even = 1
    def eve_odd(self):
        self.check(num)
        if self.even == 1:
            print('Number is even')
        else:
            print('Number is odd')
n = Number()
n.eve_odd()









