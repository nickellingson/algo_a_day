class ListNode:

    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None




class MyLinkedList: 

    def __init__(self):
        self.left = ListNode(0)
        self.right = ListNode(0)
        self.left.next = self.right
        self.right.prev = self.left


    def get(self, index: int) -> int:
        curr_node = self.left.next
        count = 0
        while curr_node:
            if count == index:
                return curr_node.value
        return -1 
    

    def addAtHead(self, val: int) -> None:
        old_head = self.left.next
        new_head = ListNode(val)
        old_head.prev = new_head
        new_head.next = old_head
        new_head.prev = self.left
        self.left.next = new_head
        

    def addAtTail(self, val: int) -> None:
        old_tail = self.right.prev
        new_tail= ListNode(val)
        old_tail.next = new_tail
        new_tail.prev = old_tail
        new_tail.next = self.right
        self.right.prev = new_tail
        

    def addAtIndex(self, index: int, val: int) -> None:
        
        count = 0
        curr_node = self.left.next
        while curr_node:
            if index == count:
                temp = curr_index.next
                new_node = ListNode(val)
                curr_index.next = new_node
                new_node.prev = curr_index
                temp.prev = new_node
                new_node.next = temp
            curr_node = curr_node.next

    def deleteAtIndex(self, index: int) -> None:
        cur = self.left.next
        while cur and index > 0:
            cur = cur.next
            index -= 1
        if cur and cur != self.right and index == 0:
            next, prev = cur.next, cur.prev
            next.prev = prev
            prev.next = next






# Your MyLinkedList object will be instantiated and called as such:
obj = MyLinkedList()
param_1 = obj.get(index)
obj.addAtHead(val)
obj.addAtTail(val)
obj.addAtIndex(index,val)
obj.deleteAtIndex(index)