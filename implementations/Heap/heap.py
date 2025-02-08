# needs to be complete binary tree
# leafs nodes need to be left to right, open is on the right
# min/max parent is more/less than children (recursive)
# implemented under the hood as an array
# left = 2 * index
# right_child = 2 * index + 1
# parent = index // 2 (floor)

# min heap
# log(n)
class Heap:
    
    def __init__(self):
        self.heap = [0]

    def push(self, val):
        self.heap.append(val)
        i = len(self.heap) - 1

        # if less than parent
        # percolate up
        while self.heap[i] < self.heap[i // 2]:
            tmp = self.heap[i]
            self.heap[i] = self.heap[i // 2]
            self.heap[i // 2] = tmp
            i = i // 2

    # move last element up to root (keep structure)
    # percolate down
    def pop(self):
        if len(self.heap) == 1:
            return None
        if len(self.heap) == 2:
            return self.heap.pop()
        
        res = self.heap[1]

        # move last element to root
        self.heap[1] = self.heap.pop()
        i = 1

        # percolate down
        while 2 * i < len(self.heap):
            if (2 * i + 1 < len(self.heap) and self.heap[2 * i + 1] < self.heap[2 * i] and self.heap[i] > self.heap[2 * i + 1]):
                # swap right child
                tmp = self.heap[i]
                self.heap[i] = self.heap[2 * i + 1]
                self.heap[2 * i + 1] = tmp
                i = 2 * i + 1
            elif self.heap[i] > self.heap[2 * i]:
                # swap left child
                tmp = self.heap[i]
                self.heap[i] = self.heap[2 * i]
                self.heap[2 * i] = tmp
                i = 2 * i
            else:
                break
        return res

    # start in the middle of array
    # build heap, percolate down
    def heapify(self, array):
        # dumby node
        array.append(array[0])

        self.heap = array
        # middle
        cur = (len(self.heap) - 1) // 2
        while cur > 0:
            # percolate down

            i = cur
            while 2 * i < len(self.heap):
                if (2 * i + 1 < len(self.heap) and self.heap[2 * i + 1] < self.heap[2 * i] and self.heap[i] > self.heap[2 * i + 1]):
                    # swap right child
                    tmp = self.heap[i]
                    self.heap[i] = self.heap[2 * i + 1]
                    self.heap[2 * i + 1] = tmp
                    i = 2 * i + 1
                elif self.heap[i] > self.heap[2 * i]:
                    # swap left child
                    tmp = self.heap[i]
                    self.heap[i] = self.heap[2 * i]
                    self.heap[2 * i] = tmp
                    i = 2 * i
                else:
                    break
            cur -= 1
        return self.heap

h = Heap()
h.heap = [1, 2, 4, 5, 6, 7, 8, 3]
print(h.heap)
h.push(3)
print(h.heap)
h.pop()
print(h.heap)
array = [3, 8, 7, 6, 5, 4, 2, 1]
print(h.heapify(array))
