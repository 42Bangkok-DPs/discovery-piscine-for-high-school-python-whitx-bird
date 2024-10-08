#!/usr/bin/env python3
x =int(input("Enter the first number: \n"))
y =int(input("Enter the second number: \n"))
results = x * y
print ( x , 'x' , y ,'=' , results)
if results > 0:
    print ("The result is positive.")
elif results < 0:
    print ("The result is negative.")
else:
    print ("The result is positive and negative.")
