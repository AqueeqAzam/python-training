import sys
print(sys.path)

from math import sqrt as s
print(s(81))

import sys
print('Hi ammarah')
sys.exit(-1)

import time
localtime = time.asctime(time.localtime())
print(localtime)

import calendar
cal = calendar.month(2022, 7)
print(cal)

import getpass
password = getpass.getpass(input('Enter the password:'))
if password == 'tyson':
    print('welcome to Aqueeq asssylm')
else:
    print('wrong password')

import subprocess
result = subprocess.run('ls')
print(result)
