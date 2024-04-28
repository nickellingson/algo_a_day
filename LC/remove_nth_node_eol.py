# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # create a dummy node
        # create two pointers
        # move pointer n down the list
        # move both pointers until the end
        # slow pointer will be in the right spot next
        # remove pointer by doing .next = .next.next

        dummy = ListNode(val = 0, next = head)
        left = dummy
        right = head
        count = 0
        while count < n and right:
            right = right.next
            count += 1

        while right:
            right = right.next
            left = left.next

        left.next = left.next.next
        
        return dummy.next