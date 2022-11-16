
#####COMMON MATHS FUNCTIONS###

#ABS FUNC- stands for absloute value

my_num = -5
print(abs(my_num))

#POW FUNCTION

print(pow(3, 2)) #its gonna be a 3^2, it makes number powers
print(pow(8, 10))

#MAX FUNC - IT TELLS US HIGHER NUMBER
print(max(8, 10))
#Min FUNC - IT TELLS US lower NUMBER
print(min(8, 10))

 ##ROUND FUNC

print(round(3.2)) #its just gonna follow stANDARD rounding rules
print(round(3.8))

#import funtion-

from math import *

#floor func basically chop off decimal point
my_num =-5
print(floor(3.7))

#ceil func.- it just round the number up no matters what

my_num =-5
print(ceil(3.7))

# square root
my_num =-5
print(sqrt(42))
print(sqrt(40))

#input function
name =  input("enter your name: ")
print("hello " + name)

name =  input("enter your name: ")
print("hello " + name + " you are a beautiful soul ! ")

name =  input(" enter your name: ")
age =  input(" enter your age: ")
print("hello " + name + " you are a beautiful soul ! " + age +" year old" )

# with integer type
num1 =  input("enter a number: ")
num2 =  input("enter another number: ")
result = int(num1) + int(num2)
print(result)
