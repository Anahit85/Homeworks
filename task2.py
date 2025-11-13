#Homework 7-8
#1
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
print("Sum:", a + b)
#2
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
print("Difference:", a - b)
#3
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
print("Product:", a * b)
#4
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
print("Division result:", a / b)
#5
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Integer part of division:", a // b)
#6
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Remainder:", a % b)
# 7
a= int(input("Enter first number: "))
b= int(input("Enter second number: "))
print("Integer part power:", a ** b)
# 8
a = int(input("Enter first number: "))
print("Remainder:", a **3)
#9
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
print('sum:', (a+b)*c)
#10
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
print('sum:', (a+b+c)/3)
#11
a = int(input("Enter first number: "))
a+=5
print(a)
#12
a = int(input("Enter first number: "))
a*=a
print(a)
#13
a = int(input("Enter first number: "))
a/=2
print(a)
#14
a = int(input("Enter first number: "))
b=int(input("Enter second number: "))
print(a<b)
#15
a = int(input("Enter first number: "))
b=int(input("Enter second number: "))
print(a==b)
#16
a = int(input("Enter first number: "))
b=int(input("Enter second number: "))
print(a!=b)
#17
a=input("Enter first string: ")
b=input("Enter second string: ")
print(a is b)
#18
a = input("Enter first string: ")
b = input("Enter second string: ")
print(a is not b)
#19
a = input("Enter first string: ")
b = input("Enter second char: ")
print(b in a)
#20
a = input("Enter first string: ")
b = input("Enter second char: ")
print(b not in a)
#21
a = input("Enter first string: ")
print('a' in a and 'b' in a)

#22
a = int(input("Enter a number: "))
if a > 0:
    print('positive number' )

else:
    print('negative number')
#23
a = int(input("Enter a number: "))
if a % 2 == 0:
    print('even number')
else:
    print('odd number')
#24
a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
if a > b:
    print('greater then a')
else:
    print('b is greater then number')
#25
a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
c = int(input("Enter a number: "))
if a > b and a > c:
    print('greater is a')
elif b > a and b > c:
    print('greater is b')
else:
    print ('greater is c')
#26
a = int(input("Enter a number: "))
if a > 0:
    print ('a is positive')
elif a < 0:
    print ('a is negative')
else:
    print ('a is zero')
#27
a = int(input("Enter a number: "))
if a >= 90 and a <= 100:
    print(' Excellent')
elif a >= 70 and a <= 89:
    print(' Good')
elif a >= 50 and a <= 69:
    print(' Average')
elif a >=0 and a <= 49:
    print(' Fail')
else:
    print('Wrong input')

#28
a = int(input("Enter a number: "))
if a >= 10000 and a <50000:
    print('10%')
elif a >= 50000:
    print('20%')
else:
    print('0%')
#29
a = int(input("Enter a number: "))
b = input("Has a passport: it could be yes or no ")

if a >= 18:
    if b == 'yes':
        print('YES')
    else:
        print('NO')
else:
    print('NO')
# 31
a = int(input("Enter a number: "))
print('positive') if a > 0 else print('negative')

#34
a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
c = int(input("Enter a number: "))
if a > b:
    if a > c:
        print('a is greater')
    else:
        print('a < c')
else:
    print('a <= b')