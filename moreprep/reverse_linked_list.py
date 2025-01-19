
class Node:

    def __init__(self, val):
        self.val = val
        self.next = None

    
class Solution:

    def reverse_list(self, head):
        
        # Null 1 -> 2 -> 3

        prev = None
        curr = head

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev


    def print_list(self, head):
        curr = head
        while curr:
            print(curr.val, "->", end="")
            curr = curr.next
        print("")
        

n = Node(1)
n1 = Node(2)
n2 = Node(3)
n.next = n1
n1.next = n2
s = Solution()
s.print_list(n)
new_head = s.reverse_list(n)
s.print_list(new_head)