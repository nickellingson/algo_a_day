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

global x
# test global and nonlocal
def outer_function():
    x = 5
    def inner_function(x):
        nonlocal x
        x += 5

    inner_function(x)
    print(x)

outer_function()