def is_palindrome(s):
    s = s.lower()
    return s == s[::-1]

s = "hehej"
print(is_palindrome(s))
print(s[::-1])


def reverse_words(s):
    s_lst = s.split(" ")
    return " ".join(s_lst[::-1])

s = "hello world beautiful"
print(reverse_words(s))

def remove_duplicates(nums):
    set_ = set()
    no_dupe_lst = []
    for num in nums:
        if num not in set_:
            set_.add(num)
            no_dupe_lst.append(num)
    return no_dupe_lst

print(remove_duplicates([1, 2, 3, 4, 5, 5, 3, 2, 1, 9]))

# two sum, target = 5. need [3, 2]
# target = num1 + num2
# IN_DICT(num1) = target - num2
def two_sum(nums, target):
    # loop through, store in dict if not in, val is index
    dict = {}
    for i in range(len(nums)):
        res = target - nums[i]
        if res not in dict:
            dict[nums[i]] = i
        else:
            return [dict[res], i]
    return - 1

print(two_sum([1,2,3,4, 5, 6], 3))
        

#rotate list based on n pivot
def rotate_list(nums, k):
    # 1 2 3 4 , k = 1
    # 4 1 2 3
    left_lst = []
    for i in range(len(nums) - k, len(nums)):
        left_lst.append(nums[i])
    right_lst = []
    for i in range(len(nums) - k):
        right_lst.append(nums[i])
    res_list = left_lst + right_lst
    return res_list
print(rotate_list([1,2,3,4], 2))

# incorrect, what if its even deeper
def flatten_list(nested_list):
    res_list = []
    for row in range(len(nested_list)):
        for col in range(len(nested_list[row])):
            res_list.append(nested_list[row][col])
    return res_list

# recursive solution, or while loop check if item is a list

print(flatten_list([[1,2],[3, 4],[2, [5, 6]]]))

def flatten_list2(nested_list):
    res_list = []
    for lst in nested_list:
        if isinstance(lst, list):
            res_list.extend(flatten_list2(lst))
        else:
            res_list.append(lst)
    return res_list

print(flatten_list2([[1,2],[3, 4],[2, [5, 6]]]))

test = [1,2,3,4]
print(test[1:])

# transpose
def transpose_list(list):
    rows = len(list)
    cols = len(list[0])

    return [[list[r][c] for r in range(rows)] for c in range(cols)]


list = [[1, 2, 3],[4, 5, 6]]
print(transpose_list(list))