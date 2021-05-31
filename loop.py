LOOP PROBLEMS ALL PROBLEMS CHECKED BY PYTHON INTERPRETOR:
    
1. compute first 10 natural number using while loop:
i = 0       # i = 0 means index started from zero.
while(i <= 10):
    print(i,end =" ")      # end = " " --> means it will print in horizontal line.
    i = i +1
    
 2. separate these number:
i = 0
while(i <= 10):
    print(i, end = '\t')
    i = i+1

 3. print vertically these number:
i = 0
while(i<=10):
    print(i, end = "\n")
    i = i+1

 4. compute sum and average of first 10 natural number:
i = 0
s = 0
while(i <= 10):
    s = s + i
    i = i +1
    avg = float(s)/10
    print("sum of ten natural number is", s)
    print("average of then natural number is:", avg)

# 5. compute 20 horizontal asterisks(*)
i = 0
while(i <= 20):
    print("*", end = (" "))
    i = i + 1  # if we does not give this code (i = i + 1) then it will keep on running so don't forget.

# 6. compute sum of two number using input function:
m = int(input("enter the value of first number:"))
n = int(input("enter the value of second number:"))
s = 0
while(m <= n):
    s = s + m
    m = m + 1
    print("sum = ",s)
    
# 7. enter a number and calculate their sum
sum = 0      # Initialising sum(variable) is equal to zero, it specify  that variable initial value.
num = int(input("enter the number"))
while(num != 0):
    temp = num % 10
    sum = sum + temp
    num = num / 10
    print("sum of digit is:", sum)

# 8. compute the reverse of a number
num = int(input("enter the number:"))
while(num >= 0):
    print( num, end = ",")
    num = num - 1    # this code always written below the print otherwise it will get one more index after zero.

# 9. compute the sum of 10 natural number
i = 0    # i get increase value by 1.
sum = 0
while(i <= 10):
    sum = sum + i
    print("sum of first 10 natural number is", sum)
    
 # 10. program to print natural number using for loop:
n = int(input("enter the value of n:"))
for i in range (1, n):
    print(i, end = " ")

# 11. compute same program by step method 
n = int(input("enter the value of n:"))
for i in range(1,n,2):
    print(i, end = " ")

# 12. compute the sum and average of first n natural number:
n = int(input("enter the value :"))
sum = 0
avg = 0.0
for i in range(1, n+1):
    sum = sum + i
avg = sum/i
print("here is sum of first natural number is", sum)
print("here is sum of avg is", avg)

# 13. compute table of any number
n = int(input("enter any number:"))
for i in range(1,n+1):
    print(n,'x',i, "=",n*i)



    

    
    
