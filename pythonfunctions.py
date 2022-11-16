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

