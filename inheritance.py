"""class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def display(self):
        print("Name :", self.name)
        print("Age :", self.age)

class Teacher(Person):
    def __init__(self, name, age, exp, r_area):
        Person.__init__(self, name, age)
        self.exp = exp
        self.r_area = r_area

    def displaydata(self):
        Person.display(self)
        print("Exp :", self.exp)
        print("Res-Area :", self.r_area)

class Student(Person):
    def __init__(self, name, age, course, marks):
        Person.__init__(self, name, age)
        self.course = course
        self.marks = marks
    def displaydata(self):
        Person.display(self)
        print("course :", self.course)
        print("Marks :", self.marks)

print('-----------------Teacher---------------------')
T = Teacher("Raju Kumar ", 32, 10, 'Car Driver')
T.displaydata()
S = Student("Tyson", 25, 'Bsc', 450)
S.displaydata()

# Multilevel inheritance

class Polygon:
    def get_data(self):
        raise NotImplementedError()
    def area(self):
        raise NotImplementedError()

class Rectangle(Polygon):
    def get_data(self):
        self.len = int(input('Enter the length rectangle :'))
        self.bre = int(input('Enter the breadth reactnge :'))
    def area(self):
        return self.len * self.bre
class Triangle(Polygon):
    def get_data(self):
        self.base = float(input('Enter base of triangle :'))
        self.height = float(input('Enter height of triangle :'))
    def area(self):
        return 0.5*self.base * self.height

p = Rectangle()
p.get_data()
print('Area of Rectangle id :', p.area())
t = Triangle()
t.get_data()
print("Area of Triangle is :", t.area())

class Parent:
    def __init__(self, fname, fage):
        self.name = fname
        self.age = fage

    def view(self):
        print(self.name, self.age)
class Child(Parent):
    def __init__(self, fname, fage):
        Parent.__init__(self, fname, fage)

    def view(self):
        print(self.age, self.name)

p = Parent(23, 'jack')
p.view()
c = Child(12, 'nick')
c.view()

class Student:
    def __init__(self, name, roll, course, year):
        self.name = name
        self.roll = roll
        self.course = course
        self.year = year
    def show(self):
        print('Name of the student is :', self.name)
        print('Roll of the student is :', self.roll)
        print('Course of the student is :', self.course)
        print('Year jof the student is :', self.year)
class Course:
    def __init__(self, name, year):
        self.name = name
        self.year = year
    def get(self):
        return self.name, self.year

class Dept:
    def __init__(self, name):
        self.name = name
        self.course = []
    def get(self, name, course):
        return (name, course)
    def add_course(self, name):
        self.course.append(name)
    def show_course(self):
        print('Course offered in this depatment :', self.course)

d = Dept('Mathematics')
d.add_course('Algebra')
d.add_course('Geometry')
d1 = Dept('Physics')
d1.add_course('Mechanies')
d1.add_course('Electronics')
print('Dear student the list of the courses offered by thsi university is below')
d.show_course()
d1.show_course()
s = Student('Tyson', 234, "Bsc", 2019)
s.show()"""

class Person:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex
    def display(self):
        print('Name', self.name)
        print('Age',self.age)
        print('Sex',self.sex)
class Publication:
    def __init__(self, no_RP, no_books, no_arts):
        self.no_RP = no_RP
        self.no_books = no_books
        self.no_arts = no_arts
    def display(self):
        print('Number of reserch paper published :', self.no_RP)
        print('Number of book publoication :', self.no_books)
        print('Number of reeerch articles :', self.no_arts)
class Faculty:
    def __init__(self, name, age, sex, degis, dept, no_RP, no_book, no_arts):
        Person.__init__(name, age, sex)
        self.degis = degis
        self.dept = dept
        self.pub = Publication(no_RP, no_book, no_arts)
    def display(self):
        Person.display(self)
        print("Degination", self.degis)
        print("department", self.dept)

f = Faculty('Tyon', 38, 'Mail', 'TIC', 'Computer science', 22, 1, 3)
f.display()

