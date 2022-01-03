# Calculator

def add(a,b):
    a = int(a)
    b = int(b)
    print(f"\n{a} pluss {b} is ")
    return a+b

def minus(a,b):
    a = int(a)
    b = int(b)
    print(f"\n{a} minus {b} is ")
    return a-b

def multiply(a,b):
    a = int(a)
    b = int(b)
    print(f"\n{a} multiplied by {b} is ")
    return a*b

def divide(a,b):
    a = int(a)
    b = int(b)
    print(f"\n{a} divided by {b} is ")
    return a/b

def checkNumber(a):
    try:
        a = int(a)
        if type(a) == int or type(a) == float:
            return True
        else:
            return False
    except:
        print("I can only accept numbers")

def checkFunction(f):

    if f == "+" or f == "-" or f == "*" or f == "/":
        return True
    else:
        print("Only use\n \t+ - * or / \nfor math magic")
        return False


ready = 1

while ready > 0:

    print("Welcome to the text caldulator.\n")

    first = input("enter number...  ")
    if checkNumber(first):
        fct = input ("enter function [ +  -  *  or / ]  ")
        if checkFunction(fct):
            second = input ("enter number...  ")
            if checkNumber(second):
                print("Looks good")
                if "*" in fct:
                    print(multiply(first,second))

                if "/" in fct:
                    print(divide(first,second))

                if "+" in fct:
                    print(add(first,second))
                
                if "-" in fct:
                    print(minus(first,second))



    else:
        print("Please try again")

    stop = input("Would you like to continue?? y/n ")
    
    if "n" in stop: 
        ready -= 2

    if "NO" in stop: 
        print("No need to shout.")
        ready -= 2

    if "q" in stop:
        print("You have no power here...")







