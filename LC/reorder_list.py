class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        slow = head
        fast = head.next

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        new_head = slow.next
        slow.next = None
        prev = None

        while new_head:
            temp = new_head.next
            new_head.next = prev
            prev = new_head
            new_head = temp

        second = prev
        first = head

        while second:
            temp1 = first.next
            temp2 = second.next

            first.next = second
            second.next = temp1

            first = temp1
            second = temp2