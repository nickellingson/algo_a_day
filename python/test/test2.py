# Core python
# 1
def double_elements(lst):
    new_lst = [x * 2 for x in lst]
    return new_lst

print(double_elements([1, 2, 3, 4, 5]))

# 2
def lookup_key(d, key):
    if key in d:
        return d[key]
    else:
        return "Key not found."
print(lookup_key({"hello":1, "hi": 2}, "hello"))

# Algorithms
# 1
def merge_sort(lst, s, e):
# base case e - s + 1 equal to or less than 0, return list
# call sort on split lists
# merge on both lists
# return list
# copy lists and then while loop, check value and merge
# two more while loops to clean up the non empty one

    if e - s + 1 <= 1:
        return lst
    
    # middle index
    m = (s + e) // 2

    # sort the left half
    merge_sort(lst, s, m)

    # sort the right half
    merge_sort(lst, m + 1, e)

    # merge sorted halfs
    merge(lst, s, m, e)

    return lst

def merge(lst, s, m, e):
    # Copy the sorted left and right halfs to temp arrays
    L = lst[s: m + 1]
    R = lst[m + 1: e + 1]

    i = 0 # index for L
    j = 0 # index for R
    k = s # index for arr

    # Merge the two sorted halfs into the original array
    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            lst[k] = L[i]
            i += 1
        else:
            lst[k] = R[j]
            j += 1
        k += 1
    
    # one of the halfs will have elements remaining
    while i < len(L):
        lst[k] = L[i]
        i += 1
        k += 1
    
    while j < len(R):
        lst[k] = R[j]
        j += 1
        k += 1
print(merge_sort([5, 4, 3, 2, 1], 0, 4))
    

# 2 
def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    while left <= right:
        middle = (right + left) // 2
        if arr[middle] > target:
            right = middle - 1
        elif arr[middle] < target:
            left = middle + 1
        else:
            return middle
    return -1

print(binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 11))

# File handling
# 1
# read file line by line and print each line
import os
print("current directory", os.getcwd())


def read_file(file_path):
    with open(file_path, "r") as f:
        for line in f:
            print(line, end="")
    
read_file("./test.txt")
print("")

# 2
# read csv file, return list of dictionaries
# each dictionary represents a row (im doing arrays, dict would be dumb in this case)
import csv
# w csv
def read_csv_listoflist(path):
    result_arr = []
    with open(path, "r") as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            result_arr.append([row])
    return result_arr

print(read_csv_listoflist("./Book2.csv"))     

import pandas as pd
# w pandas
def read_xlsx_pandas(path):
    df = pd.read_excel(path, sheet_name="Sheet1")
    return df
df = read_xlsx_pandas("./Book1.xlsx")
print(df)
print(df["colors"])
print([headers for headers in df])

# Error Handling
# 1
def safe_divide(a, b):
    try:
        result = a / b
    
    except ZeroDivisionError as e: 
        return e
    
    return result

print(safe_divide(2, 0))

# 2
# file not found
def open_file(file_path):
    try:
        with open(file_path, "r") as f:
            print(f)
            return "file found"
    except:
        return "no file"
    
print(open_file("./tes.txt"))

# Libraries
# 1
import itertools
# there is .permutations too
def get_combinations(lst):
    print(list(itertools.combinations(lst, 2)))

get_combinations([1, 2, 3, 4, 5])

# 2
from collections import Counter

def word_frequency(s):
    words = s.lower().split()
    return Counter(words)
print(x := word_frequency("hello hi hi hi hi hi yo hey hello")) # walrus operator
print(dict(x)) # messing around, Counter -> dictionary

# import unittest
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
    
# class TestPrime(unittest.TestCase):
#     def test_prime(self):
#         self.assertTrue(is_prime(5))
        #self.assertTrue(is_prime(6))
        #self.assertTrue(is_prime(42))

# test = TestPrime()
# test.test_prime()


# Code optimization
# 1
def sum_numbers(n):
    return n * (n + 1) // 2

print(sum_numbers(4))


# Write to a file
# 1 text file
def write_to_file(file_name):
    with open(file_name, "w") as f:
        f.write("hello in file")
        for i in range(10):
            f.write(str(i))

write_to_file("test_write.txt")

# 2 csv file
def write_to_csv(file_name, data):
    with open(file_name, "w") as csv_file:
        writer = csv.writer(csv_file)
        for row in data:
            writer.writerow(row)

csv_data = [
    ["Name", "Age", "City"],
    ["Alice", 30, "New York"],
    ["Bob", 25, "London"]
]
write_to_csv("write_csv_test.csv", csv_data)

# with pandas
def write_to_csv_pandas(file_name, data):
    df = pd.DataFrame(data)
    df = df.iloc[1:]
    print(df)
    df.to_csv(file_name, index=False)

dict_data = [
    {"Name": "Alice", "Age": 30, "City": "New York"},
    {"Name": "Bob", "Age": 25, "City": "London"},
    {"Name": "Charlie", "Age": 35, "City": "Paris"}
]
write_to_csv_pandas('panda_writing.csv', csv_data)