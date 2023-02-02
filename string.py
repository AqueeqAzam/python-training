import string

me = "hello"
i = 0
for i in me:
    print('message[', i, ']=',i)

str1 = 'hello'
str2 = 'world'
s = str1 + str2
print(s)

str = 'hello'
name = input('Enter your name')
str = str + name
str = str + 'welcome to python'
print(str)

name = 'Tyson'
age = 8
print("Name = %s and age = %d" %(name, age))

# slice operator
str = 'Python'
print('str[1:5] = ', str[1:5] )

str = "hello Ammarah"
print('str[-1] = ', str[-1])

# match function
import re
string = 'she sells sea ahells on the sea shore'
pattern1 = input('Enter first string')
if re.match(pattern1, string):
    print('match found')
else:
    print(pattern1, 'is not present in the string')
pattern2 = input('Enter second string')
if re.match(pattern2, string):
    print('match found')
else:
    print(pattern2, 'is not preset in the string')

# search function
import re
string = 'She sells sea shells on the shore'
pattern = input('Enter string:')
if re.search(pattern, string):
    print('Match found')
else:
    print('Match not found')

import re
story = " I love programming because this teach me how to think"
words = input('Enter words:')
if re.search(words, story):
    print('Words found')
else:
    print('Words not found')

import re
string = 'I was a research scholor mathematics'
pattern = 'was'
repl = 'am'
new_string = re.sub(pattern, repl, string, 1)
print(new_string)

import re
sent = 'Leaohard eular is a kind of mathematics and issac newton is a father of physics'
pattern = 'is' and 'king'
repl = 'was' and 'great in'
new_sent = re.sub(pattern, repl, sent, 2)
print(new_sent)

import re
result = re.findall('.', 'good going')
print(result)

while(1):

    name = input('Enter your name:')
    pan_no = input('Enter your pan number:')
    if name.isalpha() == False:
       print('Invalide name, you can not proceed')
       break
    else:
        if pan_no.isalnum() == False:
         print('Invalide pan number', 'please check your pan number')
         break

message = 'helloworld'
index = 0
while index < len(message):
    letter = message[index]
    print(chr(ord(letter) + 3), end = '')
    index += 1

str1 = 'ABCDEFGH'
str2 = 'ate'
for i in str1:
    print((i + str2), end = '')

def remove_vowel(s):
    new_str = ''
    for i in s:
        if i in 'aeiouAEIOU':
            pass
        else:
            new_str += i

    print('The string without vowel is :', new_str)
str = input('\n Enter string:')
remove_vowel(str)







