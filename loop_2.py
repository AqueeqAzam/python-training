"""
# Simple condition of grade of student
grade = int(input('Enter the grade'))
if grade >= 40:
    print('passed')
else:
    print('fail')

# Extend this condition with elif
grade = int(input('Enter the grade'))
if grade >= 90:
    print('first div')
elif grade >= 70:
    print('second div')
elif grade >= 50:
    print('third div')
else:
    print('fail')

# Many programs can be divided logically into three phases: An initialization phase which initializes the program variables; a processing phase which inputs data values and adjusts pro-
# gram variables accordingly; and a termination phase which calculates and prints the final results.

# To find sum and average of grade we use while loop
# initialization phase
total = 0   # sum of grades
grade_counter = 1   # number of grades entered
# processing phase
while grade_counter <= 5:
    grade = int(input('Enter grade'))
    total = total + grade
    grade_counter = grade_counter + 1
# terminating phase
avg = total / 5
print('Class average is', avg)

# To find sum and average of grade using while loop with exit condition
total = 0
grade_counter = 0
grade = int(input('Enter grades'))
while grade != -1:
    total = total + grade
    grade_counter = grade_counter + 1
    grade = int(input('Enter grade -1 to exit'))
if grade_counter != 0:
    avg = float(total)/grade_counter
    print(avg)
else:
    print('No grade were enterd')

# Break statement
for x in range(1,11):
    if x == 6:
        break
    print(x)
print('broke out of loop x =',x)

total = 0
grade_counter = 0
while 1:
    grade = int(input('Enter grade -1 to exit'))
    if grade == -1:
        break
    total += grade
    grade_counter += 1
if grade_counter != 0:
    avg = float(total)/grade_counter
    print(avg)
else:
    print('no grade entered')

neg = pos = zero =0
print('Enter -1 to exit....')
while(1):
    num = int(input('Enter anyt number:'))
    if (num == -1):
        break
    if(num==0):
        break
    elif(num>0):
        pos = pos + 1
    else:
        neg = neg +1
print('count of positive number enterd:', pos)
print('count of negative entered:', neg)
print('count of zeros entered:', zero)"""


n = int(input('Enter a number:'))
print('Hexadecimal of ' + str(n) + ':', str(hex(n)))



