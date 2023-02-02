try:
     num = int(input('Enter a number:'))
     if num >= 0:
          print(num)
     else:
          raise ValueError('Negative number is not allowesd')
except ValueError as e:
     print(e)

class TimeUp(Exception):
     pass
def message(c):
     start_timer = 0
     stop_timer = 10
     count = start_timer
     try:
          while True:
               count += 1
               if count == stop_timer:
                    raise TimeUp
     except TimeUp as t:
          print(c, end='')
for i in range(15):
               print(i)

def display(n):
     while True:
          try:
               n = n + 1
               if n == 21:
                    raise StopIteration
          except StopIteration:
               break
          else:
               print(n, end ='')
i = 0
display(i)

class invslidage(Exception):
     def display(self):
          print('sorry !!! age can be below 10.. you can not vote')

class invalidname(Exception):
     def display(self):
          print('please enter a valid name...')
try:
   name = input('Enter name:')
   if len(name) == 0:
     raise invalidname
     age = int(input('Enter age:'))
     if age < 18:

          raise invslidage
except invalidname as n:
     n.display()
except invslidage as a:
     a.display()


