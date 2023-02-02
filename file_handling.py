# simple program to open file
try:
    f = open('ty.text', 'rb')
    # raise ValueError
    print(f)
except IOError:
    print('File not found')

# write somethings in the file 
file = open('/home/tyson/typing practices.txt', 'w')
file.write('Hello all I am writtern this statement in file handling in python')
file.close()
print('Data written into file')

# read line method
file = open('/home/tyson/typing practices.txt', 'w')
lines = ['hello world', 'i am aqueeq azam']
file.writelines(lines)
file.close()
print('Data written into file')

# Add somethings in file
file = open('/home/tyson/typing practices.txt', 'a')
lines = ['hello world', 'i am aqueeq azam']
file.writelines(lines)
file.close()
print('Data written into file')

# file reading method
file = open('/home/tyson/typing practices.txt', 'r')
print(file.read(2))  # this argument read the characters
file.close()

# read all data that is written into file
file = open('/home/tyson/typing practices.txt', 'r')
print(file.readlines())  # this argument read the characters
file.close()

# read file using for loop
file = open('/home/tyson/typing practices.txt', 'r')
for i in file:
    print(i)
file.close()

# opening file using with keywords
with open('/home/tyson/typing practices.txt', 'r') as file1:
    line = file1.readline()
    words = line.split()
    print(words)

# copied data fro one file to another file
with open('/home/tyson/typing practices.txt', 'rb') as file1:
    with open('/home/tyson/python.txt', 'wb') as file2:
        buf = file1.read(10)
        file2.write(buf)
print('File copied')

with open('loop.py', 'rb') as file1:
    with open('file handling.py', 'wb') as file2:
        while True:
            buf = file1.readline()
            if len(buf) != 0:
                if buf[0] == '0':
                    continue
                else:
                    file2.write(buf)
            else: break
print('File copied')

file = input('Enter file name:')
with open('/home/tyson/typing practices.txt') as file1:
    text = file.read()
    letter = input('Enter file name:')
    c = 0
    for i in text:
        if i == letter:
            c += 1
print(letter, 'appeared', c , 'times in file')

# rename and deleting file
import os
os.rename('basic.py', 'hello.py')
print('File renamed')

import os
os.mkdir('New dir')
print('Directery created')

import os
os.mkdir('Old dir')
print('Directory created')

# Remove directory
import os
os.rmdir('Old dir')
print('Directory removed')

# join the path
import os
print(os.path.join('/home/tyson/PycharmProjects/softwaretraining/file.docx'))

# absolute path
import os
p = os.path.abspath('softwaretraining/file.docx')
print(p)

filename = input('Enter the filename:')
with open(filename) as file:
    # text = file.read()
    count_tab = 0
    count_space = 0
    count_nl = 0
    for char in file.read():
        if char == '\t':
            count_tab += 1
        if char == ' ':
            count_space += 1
        if char == '\n':
            count_nl += 1
print(count_tab)
print(count_space)
print(count_nl)


