import numpy as np

# method resolution order (mro) & global interpreter logic (gil)

# Show me three different ways of fetching every third item in the list
_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]



# read a csv file, have fun with it

# read a json file, have fun with it

# write a decorator

# write a simple function and test

# multiple files with importing. import other modules

# facade pattern

# print 1 - 10

# print factorial of n

# print fibbonacci of n

# fizzbuzz

# reverse list except one

# iterate over set, tuples, dict, list

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