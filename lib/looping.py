#!/usr/bin/env python3

def happy_new_year():
    i = 10
    while i > 0:
        print(f"{i}")
        i -= 1
        if i == 0:
            print("Happy New Year!")

#int_list([1, 2, 3, 4, 5])

def square_integers(int_list):
    int_list = [int**2 for int in int_list]
    return int_list

def fizzbuzz():
    i = 0
    while i > 100:
        if i % 3 == 0:
            print ("Fizz")
        elif i % 5 == 0:
            print ("Buzz")
        elif i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        else:
            print(f"{i}")
