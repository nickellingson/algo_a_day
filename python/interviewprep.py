# Core Python Concepts
# DATA STRUCTURES
lst = [1,2,3]
tup = (1, 2, 3)
dict = {"a": 1, "b": 2}
sets = {1, 2, 3}

# accessing, slicing, lookups, updates, set operations (union, intersection, difference)
# loops, list comprehensions, lambda, map, filter, functools.reduce(), generator

l = [1,2,3]
def mult(n):
    return n * 3
new_l = map(mult, l)
print(list(new_l))


subtract = lambda z, j : z - j
print(subtract(3, 1))

add = lambda x, y: x + y
print(add(5, 3))

import functools

def mult2(n, acc):
    return n * acc

reduce_list = [1, 2, 3 ,4, 5, 6, 7]
red = functools.reduce(mult2, reduce_list)
print("reduce ", red)

# implement reduce
# takes in function and list

impl_reduce_list = [1, 2, 3, 4, 5, 6, 7]

def impl_reduce(fn, list):
    res = 1
    for i in list:
        res = fn(i, res)
    return res   

print("impl reduce", impl_reduce(mult2, impl_reduce_list))


# generator
def my_generator(n):
    for i in range(n):
        yield i

_generator = my_generator(3)
print(_generator) # generator object

for value in _generator:
    print(value)

# another generator
def gen(n):
    for i in range(n):
        yield(i)
g = gen(5)
for i in g:
    print(i)

# numpy
import numpy as np

# Create a 1D NumPy array of floats
arr = np.array([1.0, 2.0, 3.5, 4.2])
print(arr)               # [1.  2.  3.5 4.2]
print(arr.dtype)         # float64 (depending on your system)
print(arr.shape)         # (4,)  -> 1D array of length 4

# Vectorized operation (element-wise multiplication by 2)
arr2 = arr * 2
print(arr2)              # [2.  4.  7.  8.4]
# vs normal array
narray = [1,2,3]
print(narray * 2)        # [1, 2, 3, 1, 2, 3]

# In-place addition
arr += 10
print(arr)               # [11. 12. 13.5 14.2]



# decorator
# to modify a function implementation behavior without changing the underlying source code by wrapping the function
# for logging, access control, memoization, and more
def decorator_logger_function(func):
    def wrapper():
        print("hi from wrapper, running function (before)")
        func()
        print("hi from wrapper, function done (after)")
    return wrapper

@decorator_logger_function
def test_function():
    print("hello from function")

test_function()

# strings tuples are immutable
# fstring
fstring = f"the = {5 == 4}"
print(fstring)

# list comprehension
arr = [[0] * 4 for i in range(4)] # 4 X 4 list
print(arr)

# ALGORITHMS
# sorting, searching, recursion
# array and hashmap, linked list, merge sort, binary search, tree bfs and dfs, recursion


# FILE HANDLING
# with open, writing, parsing csv, and json

# ERROR HANDLING
# try, except, finally
try:
    x = 1 /0
except ZeroDivisionError:
    print("Cannot divide by zero!")
finally:
    print("This will always execute")


try:
    print(" do something, success")
except NameError:
    print(NameError, "error")
except:
    "other error"
else:
    "if good to go and no error, this will run"

x = 5
if x < 0:
    raise Exception("error x < 0")

if not type(x) is int:
    raise TypeError("only integers allowed")


# LIBRARIES
# numpy and pandas
# itertools: permutations, combinations, product
# collections: Counter, defaultdict, deque
# math: sqrt, factorial, gcd, constants (pi, e)
# os and sys: file paths, os walk, system information, environment variables
# functools: partial, reduce, wraps

# TESTING
# unittest, pytest
import unittest
def add(a, b):
    return a + b

class TestAddFunctions(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)

# if __name__=="__main__":
    # unittest.main()


# test global and nonlocal
def outer_function():
    x = 5
    def inner_function():
        nonlocal x
        x += 5

    inner_function()
    print(x)

outer_function()

# module contains functions, classes, and variables
# usually a single file

# packages contain multiple modules, subpackages, and maybe __init__.py
'''
my_package/
├── __init__.py
├── module_a.py
├── module_b.py
└── subpackage/
    ├── __init__.py
    └── module_c.py

import my_package
from my_package import module_a
from my_package.subpackage import module_c
'''

# variables and naming convention
# single leading underscore prefix is used for internal use within a module
_for_internal_use = 1

# keyword already take
class_ = "class"

# avoid attribute collisions in subclassing
__var = "var"

# dunder or magic method, python interals or special protocol
# __init__ -> constructor
# __str__ -> to string method
# __main__
# __name__ module attribute

# code won't execute unless ran directly
# if __name__ == "__main__":
# python filename.py
# keeps library code (functions, classes, etc.) seperate from script-running code

# self is the current instance

# @staticmethod = normal function does not receive automatice references like self (helper functions)
# @classmethod = bound to class, receives cls (class itself not instance)
'''
@classmethod
def from_string(cls, data_str):
    # Parse data_str and create an instance
    return cls(...)
'''


# Namespaces
# mapping from name (identifiers) to objects
# like a dictionary that keeps track of which name points to which object
# len(), print(), Exception
x = 50  # Global namespace

def outer():
    x = 25  # Enclosing (outer) scope

    def inner():
        x = 10  # Local (inner) scope
        print("inner x =", x)
    inner()
    print("outer x =", x)

outer()
print("global x =", x)

# MRO = Method Resolution Order
# order in which Python looks up methods and attributes on a class and its parent classes (i.e. superclasses)
# c3 linearization algorithm, create a single linearized order for searching parents attributes
# MyClass.__mro__


# inheritance, super, and mro
class A:
    def greet(self):
        print("Hello from A")

class B(A):
    def greet(self):
        print("Hello from B")
        super().greet() # call next in MRO line, parent

# class C(A):
#     def greet(self):
#         print("Hello from C")
class D(B):
    pass
d = D()
d.greet()
print(D.mro())

# python garbage collection
# uses reference counting, tracks how many references (variables, data structures, etc) are pointing to it
def create_list():
    x = [1, 2, 3]
    return x

lst = create_list()  # Reference count for [1, 2, 3] is at least 1
lst = None           # Reference count goes to 0, memory can be freed

# cyclical garbage collection, scans to find cycle and no external references
# a.ref = b
# b.ref = a

# generation, how long an object has survived garbage collections

