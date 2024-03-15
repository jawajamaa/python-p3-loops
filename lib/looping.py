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

# def fizzbuzz_Printer():
#     for i in range(100):
#         print (fizzbuzz(i))


# def fizzbuzz(i):
#     if i % 3 == 0 and i % 5 == 0:
#         return "FizzBuzz"
#     elif i % 3 == 0:
#         return "Fizz"
#     elif i % 5 == 0:
#         return "Buzz"
#     else:
#         return f"{i}"

def fizzbuzz():
   i = 1
   while i <= 100:
       if i % 3 == 0 and i % 5 == 0:
           print("FizzBuzz")
       elif i % 3 == 0:
           print ("Fizz")
       elif i % 5 == 0:
           print ("Buzz")
       else:
           print(f"{i}")
       i += 1
