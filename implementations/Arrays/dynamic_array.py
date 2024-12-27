class Array:

    def __init__(self):
        self.capacity = 2
        self.length = 0
        self.arr = [0] * 2

    # Method
    # insert n at end
    def pushback(self, n):
        if self.length == self.capacity:
            self.resize()
        self.arr[self.length] = n
        self.length += 1
    
    # create new array and double capacity
    def resize(self):
        self.capacity = 2 * self.capacity
        newArr = [0] * self.capacity

        # copy over elements
        for i in range(self.length):
            newArr[i] = self.arr[i]
        self.arr = newArr

    # remove last element in array
    def popback(self):
        if self.length > 0:
            self.length -= 1

    # get value
    def get(self, i):
        if i < self.length:
            return self.arr[i]
    
    # Insert at n
    def insert(self, i, n):
        if self.length == self.capacity:
            self.resize()
        for index in range(self.length - 1, i - 1, -1):
            self.arr[index + 1] = self.arr[index]

        self.arr[i] = n



# Create object instance
a = Array()
print(a.arr)