print("----------")
print((          "|"),("       |"))
print((         "|"),("       |"))
print((         "|"),("       |"))
print("----------")

print("       /")
print("      /")
print("     /")
print("    /")
#print("  /")

print ("hello world")


#variables
is_male = True
character_name = "jhon"
character_age ="65"
print(character_name+character_age+"is ver jolly and nice person")

#STRINGS

print("giraffe Academy")

print("giraffe\"Academy")#\n for new line & qutation " mark
print("giraffe\Academy") # for backslash\
print("giraffe\Academy")

print("giraffe\n Academy")#\n for new line
#######VARIABLES########

spot = "giraffe,Academy"
print(spot)

####CONCATNATION####

spot = "giraffe,Academy"
purpose = " teaching"
print(spot + purpose)


###UPPER LOWER CASE#####

spot = "giraffe,Academy"
print(spot.upper())

spot = "GIRAFFE,ACADEMY"
print(spot.lower())

#####BOOLEAN TYPE OF UPPER/LOWER CASE

spot = "giraffe,Academy"
print(spot.isupper())

spot = "GIRAFFE,ACADEMY"
print (spot.isupper()) #its True

spot = "giraffe,Academy"
print (spot.upper().isupper()) #its True


 #####FUNCTIONS######

### CHECKING STRING LENGTH FUNCTION

spot = "GIRAFFE,ACADEMY"
print(len(spot))

    #INDIVIDUAL CHARACTERS

spot = "GIRAFFE,ACADEMY"
print(spot[4])

spot = "GIRAFFE,ACADEMY"
print(spot[1])

####INDEX FUNCTION- tells you where is specific character or string is located inside of our string

spot = "GIRAFFE,ACADEMY"
print(spot.index("G"))

spot = "GIRAFFE,ACADEMY"
print(spot.index("A"))

spot = "GIRAFFE,ACADEMY"
print(spot.index("ACA"))

##REPLACE FUNC.- will replace your string words

spot = "GIRAFFE,ACADEMY"
print(spot.replace("GIRAFFE", "ELEPHANT"))

#####NUMBERS IN PYTHON BASICS AND TYPES AND FUNCTIONS FOR MATHEMATICAL OPERATIONS

print(2)
print(.882)
print(-2.876)

##BASIC ARITHMATIC

print(2 + 4)
print(2 - 4)
print(2/4)
print(2*4)

####MORE COMPLEX MATHS

print(2 + 4 * 5) # PYTHON USES BODMAS

#SPECIFY ORDER

print(2 * (4 + 2)) #USE ()PARANTHESIS FOR CHANGE ORDER FOR SUM

##MODULOUS FUNCTION

print(2 % 7) #THIS BASICALLY GOING TO GIVE US REMAINDER
print(8 % 2)

my_num = 5
print(str (my_num))

my_num = 5
print(str (my_num) + " is my favourite")

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

# with float data type
num1 =  input("enter a number: ")
num2 =  input("enter another number: ")
result = float(num1+num2)
print(result)

######## MAD LIBS GAME ######


common_noun = input("enter a common noun:")
funny_living_place = input("enter a funny living place: ")
any_funny_swimming_place = input("enter a any_funny_swimming_place: ")
funny_climmbing_things = input("enter a funny_climmbing thing: ")

print("There was a little " + common_noun )
print("He lived in a " + funny_living_place)
print("He swam in a " + any_funny_swimming_place )
print("He climbed on the  " + funny_climmbing_things)

#list

veggies = [" gobi ", "bhindi ", "aloo ","laah ","blaah "]
print(veggies) #grabbing whole list

veggies = [" gobi ", "bhindi ", "aloo ","laah ","blaah "]
print(veggies[1])  #grabbing from 1 list (it works like 0,1,2,3,4,5)

veggies = [" gobi ", "bhindi ", "aloo ","laah ","blaah "]
print(veggies[1 :]) #grabbing from 1 to rest all list

veggies = [" gobi ", "bhindi ", "aloo ","laah ","blaah "]
print(veggies[1:4]) #grabbing from 1 to till 4 list

# modification of value

veggies = [" gobi ", "bhindi ", "aloo ","laah ","blaah "]
veggies [1] ="apple"
print(veggies [1])

###list fuctions
#how to add another list into list
veggies = [" gobi ", "bhindi ", "aloo ","laah ","blaah "]
quantity = ["1kg","2kg","3kg","4kg","5kg"]
veggies.extend(quantity)
print(veggies)

#append function
veggies = [" gobi ", "bhindi ", "aloo ","laah ","blaah "]
veggies.append("spinach")
print(veggies)

#insert function

veggies = [" gobi ", "bhindi ", "aloo ","laah ","blaah "]
veggies.insert(1, "spinach")
print(veggies)

#remove func

veggies = [" gobi ", "bhindi ", "aloo ","laah ","blaah "]
veggies.remove(" gobi ")
print(veggies)

#clear func - to clear all list
veggies = [" gobi ", "bhindi ", "aloo ","laah ","blaah "]
veggies.clear()
print(veggies)

#pop func - this remove the last element from the list
veggies = [" gobi ", "bhindi ", "aloo ","laah ","blaah "]
veggies.pop()
print(veggies)

#if the certain element exist in the list

veggies = [" gobi ", "bhindi ", "aloo ","laah ","blaah "]
print(veggies.index("aloo "))

veggies = [" gobi ", "bhindi ", "aloo ","laah ","blaah "]
print(veggies.index("laah "))

#count specific itmes in list

veggies = [" gobi ", "bhindi ","bhindi ","bhindi ", "aloo ","laah ","blaah "]
print(veggies.count("bhindi "))

#sort- it will put list in assending order
veggies = ["gobi ", "bhindi ","bhindi ","bhindi ", "aloo ","laah ","blaah "]
veggies.sort()
print(veggies)

veggies = ["gobi ", "bhindi ","bhindi ","bhindi ", "aloo ","laah ","blaah "]
print(veggies.sort())
print(veggies)

quantity = [11,2,3,44,15]
quantity.sort()
print(quantity)

##reverse func
veggies = ["gobi ", "bhindi ","bhindi ","bhindi ", "aloo ","laah ","blaah "]
veggies.reverse()
print(veggies)

#copy func
veggies = ["gobi ", "bhindi ","bhindi ","bhindi ", "aloo ","laah ","blaah "]
veggies2 = veggies.copy()
print(veggies2)

###TUPPLES - ONCE you create the tupples, it's as it is you can not change them further

coordinates = (4, 5)
print(coordinates[0])

coordinates = (4, 5)
coordinates[1] = 19
print(coordinates[1]) #that will give error bcz tupples can never be change 

coordinates = [4, 5]
coordinates[1] = 19
print(coordinates[1]) #list can be change and modified


coordinates =[(4, 5), (3, 4), (2, 6), (3, 7)]
coordinates[1] = 19
print(coordinates[1])

#####python functions - collection of codes which perform specific tasks

def say_hey(): #def is keyword and say_hey is function name
    print("hello user") #all the code should should be inside the function, needs to be indented.
say_hey() #calling function


###flow of func
def say_hey():
    print("hello user")

print("boo")  # first will excute print statement
say_hey() #then it jump on to function call
print("helo") # then again printing out print statement

##naming function
def say_hey():
    print("hello user")

print("boo")
say_hey()
print("helo")

###passing parameters
def say_hey(name, age): #you can take multiple parameters
    print("hello " + name + ", your age is " + str(age))

say_hey("ru ", 20)
say_hey("su ", 30)


def lays(name, brand):
    print("new crips " + name + "from" + brand)

lays("kurkure "," ITC")

###return statement it allows us to create a value for a variable.

def cube(num):
    return num*num*num
print(cube(3))


def cube(num):
    return num*num*num
result = cube(3)
print(result)

###if statement#####

#if statement with a boolean variable

is_male = False

if is_male:
    print("you are male")

is_male = True

if is_male:
    print("you are male")

####IF ELSE

is_male = False
if is_male:
    print("you are male")
else:
    print("you are not male")



box = input("enter your box color-")
red = box
if box is red:
     print ("its a blue box ")
elif its not blue :
    print("its not a blue box ")

else:
    print("sorry its a different color box ")





box = input("enter your box color-")
red = box
if box is red  :
     print ("its a blue box ")
else:
    print("not blue ") 

###OR STATEMENT

is_male = False
is_tall = False
if is_male or is_tall:
    print("you are male")
else:
    print("you are not male")

###and keyword basically it execute if both of the conditions is true

is_male = True
is_tall = True
if is_male and is_tall:
    print("you are male")

elif is_male and not(is_tall):
    print("you are a short")

else:
    print("you are not male")


def max_num(num1,num2,num3):
    if num1>=num2 and num2>=num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3
print(max_num(1,2,5))


#########BUILIDING A CALCULATOR###########
#ADD ,SUBTRACT , MINUS ,DIVIDE
num1 = float(input("enter first number: "))
op = input("enter operator: ")
num2 = float(input("enter second number: "))
if op == "+":
    print(num1+num2)
elif op == "-":
    print(num1-num2)
elif op =="/":
    print(num1/num2)
elif op == "*":
    print(num1*num2)
else:
    print("invalid operator")

#######DICTIONARIES##########


monthconversations = {
    "jan": "january",
    "feb": "febuary",
    "mar": "march",
    "apr": "april",
    "may": "may",
}

print(monthconversations["jan"])



monthconversations = {
    "jan": "january",
    "feb": "febuary",
    "mar": "march",
    "apr": "april",
    "may": "may",
}
print(monthconversations["jan"])
