import numpy as np

# # Creating a 1D array
# arr1 = np.array([1, 2, 3, 4])
# print(arr1)  # Output: [1 2 3 4]

# # Creating a 2D array (matrix)
# arr2 = np.array([[1, 2], [3, 4]])
# print(arr2)

# print(arr2.shape)  # (2, 2) -> 2 rows, 2 columns
# print(arr2.size)   # 4 -> Total number of elements
# print(arr2.dtype)  # int64 -> Data type of elements


# a = np.array([1, 2, 3])
# b = np.array([4, 5, 6])

# # Addition
# print(a + b)  # Output: [5 7 9]

# # Multiplication
# print(a * b)  # Output: [4 10 18]

# # Exponentiation
# print(np.exp(a))  # e^1, e^2, e^3

# A = np.array([[1, 2, 3], [4, 5, 6]])
# B = np.array([1, 2, 3])

# print(A + B)  # B is broadcasted to match A's shape

# arr = np.array([[10, 20, 30], [40, 50, 60]])

# # Accessing an element
# print(arr[1, 2])  # 60

# # Slicing (selecting a submatrix)
# print(arr[:, 1])  # [20, 50] -> Selects the second column

# arr = np.array([10, 20, 30, 40, 50])

# # Get elements greater than 25
# print(arr[arr > 25])  # Output: [30 40 50]

# A = np.array([[1, 2], [3, 4]])
# B = np.array([[5, 6], [7, 8]])

# print(np.dot(A, B))  # Matrix multiplication

# print(np.linalg.inv(A))   # Inverse of matrix A
# print(A.T)                # Transpose of A

# arr = np.array([10, 20, 30, 40, 50])

# print(arr.sum())      # 150
# print(arr.mean())     # 30.0
# print(arr.max())      # 50
# print(arr.min())      # 10
# print(arr.std())      # Standard deviation

# arr = np.arange(1, 7).reshape(2, 3)  # Reshape to 2x3
# print(arr)

# # Transpose (swap rows and columns)
# print(arr.T)

# arr = np.array([10, 20, 30, 40, 50])

# # Boolean filtering
# filtered = arr[arr > 25]  # [30, 40, 50]
# print(filtered)

# data = np.genfromtxt("large_file.csv", delimiter=",", skip_header=1)

# data = np.array([1, 2, np.nan, 4, 5])

# # Replace NaNs with mean
# data[np.isnan(data)] = np.nanmean(data)

# # Generate large random dataset
# big_data = np.random.rand(1000000)

# # Fast computations using NumPy
# mean_val = np.mean(big_data)
# sum_val = np.sum(big_data)




## Test

arr = np.array([1,2,3,4,5,6,7,8,9])
window = 3

count = 0
print(len(arr))

new_arr = np.array([])

for i in range(len(arr)):
    count += 1
    if count >= 3:
        new_arr = np.append(new_arr, np.average([i - 2 , count]))

print(np.ceil(new_arr))

# normalize the 2d array

matrix = np.array([[10, 200], [20, 400], [30, 600]])
min = np.min(matrix)
max = np.max(matrix)

# arr =
# [[1 2 3 4]
# [2 3 4 5]
# [3 4 5 6]]

# arr[0] = [1 2 3 4]
# arr[0][0] = [1]


new_arr = matrix
for x in range(len(matrix)):
    for y in range(len(matrix[x])):
        normalized = ((matrix[x][y] - min)/(max - min))
        new_arr[x][y] = normalized
print(new_arr)

# initialize array with loop
arr = [[0 for i in range(5)]] * 5
print(arr)

from collections import deque

class PracticeNode:
    
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
    
class BFS:

    def bfs(self, root):
        q = deque([root])
        while q:
            for _ in range(len(q)):

                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                print(node.val, end=" ")
            print("")
            


if __name__=="__main__":
    root = PracticeNode(10)
    root.left = PracticeNode(20)
    root.right = PracticeNode(30)
    root.left.left = PracticeNode(40)
    run = BFS()

    run.bfs(root)
