import math
#How to check the log of x to the power of y
x= int(input("Enter your first number : "))
y=int(input("Enter your second number: "))
print("{0} to the power of {1} is ".format(x,y), str(x**y))
l= math.log(x)
print("Log of {0} is ".format(x),str(l) )
