# hashmap implementation
# implemented under the hood as an array
# empty hashmap is non-zero, array could be size 2 or other size with null values
# expected worst case scenario is O(1), O(1) average case
# hashing (covert key into integer)
# there are many types of hashing functions
# use %, key % len(array) = valid index
# remainder will always be less than the mod
# Example: % 3, will produce remainder of 0, 1, or 2
# same mod? hashing collision happens
# keep track of size of array and how many keys have been inserted (capacity)
# then can resize (double), this will make it less likely for cache hits
# rehashing the array
# create linked lists for values (chained hashing)
# or use open addressing (linear probing)
# optimal size is a prime number

class Pair:

    def __init__(self, key, val):
        self.key = key
        self.val = val


class HashMap:

    def __init__(self):
        self.size = 0
        self.capacity = 2
        self.map = [None, None]

    def hash(self, key):
        index = 0
        for c in key:
            # ASCII
            index += ord(c)
        # returning index where key should be
        return index % self.capacity

    def get(self, key):
        index = self.hash(key)

        while self.map[index] != None:
            if self.map[index].key == key:
                return self.map[index].val
            index += 1
            # keep within array
            index = index % self.capacity
        return None

    def put(self, key, val):
        index = self.hash(key)

        while True:
            # empty index, assign pair to index
            if self.map[index] == None:
                self.map[index] = Pair(key, val)
                self.size += 1
                if self.size >= self.capacity // 2:
                    self.rehash()
                return
            # overwrite value
            elif self.map[index].key == key:
                self.map[index].val = val
                return

            index += 1
            # keep within array
            index = index % self.capacity

    def rehash(self):
        self.capacity = 2 * self.capacity
        newMap = []
        for i in range(self.capacity):
            newMap.append(None)
        
        oldMap = self.map
        self.map = newMap
        self.size = 0
        for pair in oldMap:
            if pair:
                self.put(pair.key, pair.val)
