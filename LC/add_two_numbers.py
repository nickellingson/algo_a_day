# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        carryover = 0
        dummy = ListNode()
        curr = dummy
        while l1 or l2 or carryover:
            if not l1:
                left = 0
            else:
                left = l1.val

            if not l2:
                right = 0
            else:
                right = l2.val

            total = left + right + carryover

            carryover = total // 10

            val = total % 10

            curr.next = ListNode(val)

            curr = curr.next

            if l1:
                l1 = l1.next
            else:
                l1 = None

            if l2:
                l2 = l2.next
            else:
                l2 = None
        
        return dummy.next