a = int(input('Enter first num:'))
b = int(input('Enter second num:'))
if a == b:
    print('Num is equal')
else:
    print('Num is not equal')

o = 'outstanding'
a = 'average'
b = 'brilliant'

cha = input('Enter character:')
if cha == 'o':
    print('Outstanding')
    
elif cha == b:
    print('brilliant')
elif cha == a:
    print('Average performance')
else:
    print('Keep practice')

cha = input('Enter a character:')
if (cha.isalpha()):
    print('This is characer')
if (cha.isdigit()):
    print('Character is digit')
if (cha.isspace()): 
    print('Character is space')

# determine wheather a digit, uppercase or lowercase
char = input('Enter character:')
if char.islower():
    print('Characters is lowercase')
elif char.isupper():
    print('Characrter is uppercase')
elif char.isdigit():
    print('Characters is digit')

else:
    print('Not entered by users') 

# This is Window 10 here
char = input('Enter characters:')
for i in char:
    if i >= 'a' and i <= 'z':
        print('characters is lowercase')
    elif i >= 'A' and i <= 'Z':
        print('Character is uppercase')
    elif i >= '0' and i <= '9':
        print('Character is digit')   
    else:
        print('not enter by user')

char = input('Enter characters:')
for i in range(len(char)):
    if i == char.isdigit():
        print()
    elif i == char.islower():
        print(i)
    elif i == char.isupper():
        print(i)
    else:
        print('Not entered by users')

# nested if statement
char = int(input('Enter score:'))
if char == 100:
    print('You hit century')
if char == 50:
    print('ypu hit half century')
if char == 20:
    print('Need work hard')

# display 10 natural numbers
for i in range(11):
    print(i, end=' ')

# print 10 natural numbers
i = 0
sum = 0
while( i <= 10):
    print(i, end=' ')
    sum = sum + i
    i = i + 1
avg = float(sum) / 10
print(sum)
print(avg)

# n = int(input('Enter value of n:'))
sum = 0
for i in range(10):
    #print(i, end=" ") 
    sum = sum + i
    print(sum, end=' ')
avg = float(sum / 10)
print(avg, end=' ')
