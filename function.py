
"""
# find square of number
def sqr(x):
    return x*x
t = int(input("enter number"))
y = sqr(t)
print('Square is',y)

# with square function
def square(x):
    return x*x
for y in range(1,11):
 t = square(y)
 print(t)

def max_value(x, y, z):
    if x>y and y>z:
        return 1
    if y>x and y>z:
        return 0
    if z>z and z>y:
        return -1
a = int(input('Enter first number'))
b = int(input('Enter sec number'))
c = int(input('Enter thi number'))
if (a==1):
    print('max is',a)
if (b == 0):
    print('max is ',b)
if (c==-1):
    print('max',c)
max_value(a, b, c)

# small random game
import random
fre1 = 0
fre2 = 0
fre3 = 0
fre4 = 0
fre5 = 0
fre6 = 0
for roll in range(1, 6001):
    face = random.randrange(1, 7)
    if face == 1:
        fre1 += 1
    elif face == 2:
        fre2 += 1
    elif face == 3:
        fre3 += 1
    elif face == 4:
        fre4 += 1
    elif face == 5:
        fre5 += 1
    elif face == 6:
        fre6 += 1
    else:
        print('Should never get here')
print(fre1)
print(fre2)
print(fre3)
print(fre4)
print(fre5)
print(fre6)

def fact(n):
    if n == 1:
        return 1
    else:
        return n*fact(n-1)
# x = int(input('Enter number'))
# t = fact(x)
# print("Factorial of number is ",t)
# or we can make short-cut
print('factorial of number',fact(5))


___________________________________________________

def add(x, y):  # taking two parameters
    return x+y
a = 10
b = 5
r = add(a, b)
print('Addition of two number is ', r)

def str():  # no argument taking so no need to return
    for i in range(5):
        print(i)
s = str()

def cube(x):
    return x*x*x
a = int (input("Enter number:"))
c = cube(a)
print('cube of number', a, '=', c)

def check(a,b):
    if a==b:
        return 0
    if a>b:
        return 1
    if a<b:
        return -1

a = 4
b = 6
c = 2
res = check(a,b)
if res == 0:
    print('a is equal to b')
if res == 1:
    print('a is greater than b')
if res == -1:
    print('a is less than b')

def swape(a,b):
    a,b = b,a
    print('Number after swaping', a, b)
a = 5
b = 6
print('number after swaping', a, b)
swape(5, 6)

div_2_4 = []
for i in range(2, 22):


    if i%2==0 or i%4 ==0:

        div_2_4.append(i)
print(div_2_4)

# Recursion
def fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n*fact(n-1)
n = int(input('Enter number:'))
print('Factorial of', n, 'is', fact(n))

def exp(x, y):
    if y == 0:
        return 1
    else:
        return x**y
x = int(input('Enter x:'))
y = int(input('Enter y:'))
e = exp(x, y)
print('Exopennts is ', e)

def gcd(x, y):
    rem = x%y
    if rem ==0:
        return y
    else:
        return gcd(y, rem)
x = int(input('Enter number'))
y = int(input('Enter numbrer'))
g = gcd(x,y)
print('GCD od two number is:', g)


# cyber security code

def configure_intf(intf, ip, mask):
    print('interface', intf)
    print('ip address', mask)

configure_intf('F0/0', '10.1.1.1', '255.255.255.0')

def configure_inif(intf_name, ip, mask):
    config = f"interface{intf_name}\n ip address {ip}{mask}"
    return config

result = configure_inif('F0/0', '10.1.1.1', '255.255.255.0')
print(result)

def check_passwd(username, password):
    if len(password)<8:
        print('password is to short')
        return False
    elif username in password:
        print('password contains username')
        return False
    else:
        print(f'Password for user {username} has passed all checks')
        return True

check_passwd('tyson', 12345)

def check_passwd(username, password, min_length = 8, check_username = True):
    if len(password) < min_length:
        print('password is to short')
        return False
    elif check_username and username in password:
        print('password contains username')
        return False
    else:
        print(f'passwors for user {username} has passed all checks')
        return True
check_passwd('nata', '123456789', min_length=9)

_________________________________________________________

# some useful function
# zip function
d_keys = ['hostname', 'location', 'vendor', 'model', 'IOS', 'IP']
d_vales = ['los angee_1', 'los angelses', 'cisco', '4451', '14.6', '10.224.0.1']
l = list(zip(d_keys, d_vales))
print(l)
print('\n')
d = dict(zip(d_keys, d_vales))
print(d)"""


