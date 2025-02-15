# Core Python Concepts
# DATA STRUCTURES
lst = [1,2,3]
tup = (1, 2, 3)
dict = {"a": 1, "b": 2}
sets = {1, 2, 3}

# accessing, slicing, lookups, updates, set operations (union, intersection, difference)
# loops, list comprehensions, lambda, map, filter, functools.reduce(), generator

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
# map bfs (adjacency list)

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


# inheritance
class A:
    def greet(self):
        print("Hello from A")

class B(A):
    def greet(self):
        print("Hello from B")

class C(A):
    def greet(self):
        print("Hello from C")
class D(B, C):
    pass
d = D()
d.greet()
print(D.mro())