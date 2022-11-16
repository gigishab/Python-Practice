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

