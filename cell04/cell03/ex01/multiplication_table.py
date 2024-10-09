#!/usr/bin/env python3
try:
    Num = int(input("Enter a number \n"))
    for number in range(0,10):
        print(Num, 'x', number, '=', Num * number)
except:
    print("Error input ")
