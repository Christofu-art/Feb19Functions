def battery_check(num):
    if num >= 100:
        return "Battery full"
    elif num >= 50:
        return "Battery good"
    else:
        return "Battery low"

def mult_check(bobby):
    for i in range(10):
        print(i, " * ", bobby, " = ", bobby*i)
       
mult_check(3)

def vowels(word):
    for i in word:
       
        if i == "a":
            print (" * ")
        elif i == "e":
            print( " * ")
        elif i == "i":
            print (" * ")
        elif i == "o":
            print( " * ")
        elif i == "u":
            print (" * ")
        else:
            print(i)

vowels("gary lonebear apples")

def pizza_time(d, p):
    r=d/2
    area = 3.14 *r*r
    print (p/area)
result = pizza_time(12, 6)
print (" ", result)
