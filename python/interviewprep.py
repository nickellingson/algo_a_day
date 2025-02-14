# Core Python Concepts
# DATA STRUCTURES
lst = [1,2,3]
tup = (1, 2, 3)
dict = {"a": 1, "b": 2}
sets = {1, 2, 3}

# accessing, slicing, lookups, updates, set operations (union, intersection, difference)
# loops, list comprehensions, lambda, map, filter, functools.reduce()

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

