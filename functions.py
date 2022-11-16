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