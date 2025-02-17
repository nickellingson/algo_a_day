import numpy as np
import unittest

# method resolution order (mro) & global interpreter logic (gil)

# Show me two different ways of fetching every third item in the list
_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new_list = []
for i in range(len(_list)):
    if (i + 1) % 3 == 0:
        new_list.append(_list[i])
print(new_list)

new_list = []
print([_list[i] for i in range(len(_list)) if (i + 1) % 3 == 0])


# read a csv file, have fun with it

# read a json file, have fun with it

# write a decorator
# logging
def dec_logger(fn):
    def wrapper():
        print("function started")
        fn()
        print("function ended")

    return wrapper

@dec_logger
def func_test():
    print("running")

func_test()


# write a simple function and test
class TestMul(unittest.TestCase):
    def mult(self):
        self.assertEqual(5, mult(5, 1))

def mult(x, y):
    return x * y


# multiple files with importing. import other modules
# facade pattern
# import importer
# or
from importer import Talk 
class Water():
    def drink(self):
        print("drinking")

class Food():
    def eat(self):
        print("eating")

class Facade():

    def __init__(self):
        self.f = Food()
        self.w = Water()
        # imported
        # self.t = importer.Talk()
        self.t = Talk()

fac = Facade()
fac.f.eat()
fac.t.speaking()



# print 1 - 10
for i in range(1, 11):
    print(i, end=" ")
print("")

# print factorial of n

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result = result * i
    return result
print(factorial(1))
print(factorial(2))
print(factorial(3))
print(factorial(4))
print(factorial(5))
print(factorial(6))

# print fibbonacci of n
# 1 1 2 3 5 8 13
def fib(n):
    # base case
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)
print("fib")
print(fib(1))
print(fib(2))
print(fib(3))
print(fib(4))
print(fib(5))
print(fib(6))


# fizzbuzz
# Given an integer n, for every positive integer i <= n, the task is to print,
# “FizzBuzz” if i is divisible by 3 and 5,
# “Fizz” if i is divisible by 3,
# “Buzz” if i is divisible by 5
# “i” as a string, if none of the conditions are true.

# def fizzbuzz(n):
#     for i in range(1, n + 1):
#         if i % 3 == 0 and i % 5 == 0:
#             print("FizzBuzz")
#         elif i % 3 == 0:
#             print("Fizz")
#         elif i % 5 == 0:
#             print("Buzz")
#         else:
#             print(f"{i}")
# fizzbuzz(20)

# reverse list except one
special_index = 1
rev_list = [1, 2, 3, 4, 5, 6, 7]
new_list = []
new_index = len(rev_list) - special_index
for i in range(len(rev_list), 0, -1):
    if i == new_index:
        new_list.append(rev_list[special_index])
    new_list.append(i)
    
print(new_list)


# iterate over set, tuples, dict, list
s = set([1, 2, 3, 4, 5])
for n in s:
    print(n, end=" ")
print()
d = {"yo": 1, "hi": 2}
for key, val in d.items():
    print(key, val, end=" ")
print()
l = [i for i in range(5, 0, -1)]
for i in l:
    print(i, end=" ")
print()
# reverse linked list
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
    
def reverse_list(head):
    curr = head
    prev = None
    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    return prev

def print_list(head):
    curr = head
    while curr:
        print(curr.val, " -> ", end=" ")
        curr = curr.next

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
print_list(head)
print()
print_list(reverse_list(head))
print()

# list, set, and dictionary comprehensions
array_2d = [[0] * 4 for i in range(4)]
print(array_2d)
# edit array 1, 2 ... 16
i = 0
for row in range(len(array_2d)):
    for col in range(len(array_2d[row])):
        i += 1
        array_2d[row][col] = i
print(array_2d)

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# take list and ^2 all of the elements
squared_list = [i * i for i in my_list]
print(squared_list)
# or
np_arr_squared = np.array(my_list)
print(np.square(my_list))

# set comprehension
_set = set(i for i in range(5))
print(_set)

# dictionary comprehension
squares = {x: x*x for x in range(6)}
print(squares)

# convert list to a dictionary, capture length of string
fruits = ["apple", "banana", "cherry", "date"]
fruit_lengths = {fruit : len(fruit) for fruit in fruits}
print(fruit_lengths)

# with condition
numbers = range(10)
# even squares
even_squares_dict = {number: number * number for number in numbers if number % 2 == 0}
print(even_squares_dict)

# enumerate 
words = ["alpha", "beta", "gamma"]
indexed_words = {i: w for i, w in enumerate(words)}

# file io with generator
# def read_large_file(file_path):
#     """Yield one line at a time from a large file."""
#     with open(file_path, 'r') as f:
#         for line in f:
#             yield line.strip()

# def process(line):
#     pass
# # Usage
# for line in read_large_file("big_data.txt"):
#     process(line)  # Do something with each line