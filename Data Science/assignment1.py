import math
#How to check the log of x to the power of y

for p in range(1,10,1):
    
    while True:
        try:
            x=int(input("Enter your first number : "))
        except ValueError:
            print(' Print Please enter a valid number')
            continue
        else:
            break



    while True:
        try:
            y=int(input("Enter your Second number : "))
        except ValueError:
            print(' Print Please enter a valid number')
            continue
        else:
            break

    print("{0} raised to the power of {1} is : ".format(x,y),pow(x, y))
    l= math.log(x)
    print("Log of {0} is ".format(x),str(l) )