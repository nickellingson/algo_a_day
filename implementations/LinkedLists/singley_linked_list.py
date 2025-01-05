class ListNode:

    def __init__(self, value):
        self.value = value
        self.next = None


class SinglyLinkedList:

    def __init__(self):
        self.head = ListNode(-1)
        self.tail = self.head

    def insert_end(self, val):
        self.tail.next = ListNode(val)
        self.tail = self.tail.next

    def remove_at_index(self, index):
        curr_node = self.head
        count = 0

        while curr_node and count < index:
            count += 1
            curr_node = curr_node.next

        if curr_node and curr_node.next:
            if curr_node.next == self.tail:
                self.tail = curr_node
                #curr_node.next = None
            #else:
                curr_node.next = curr_node.next.next


    def print_list(self):
        curr_node = self.head.next
        while curr_node:
            if curr_node == self.head.next:
                print(curr_node.value, "(head) -> ", end="")
            elif curr_node == self.tail:
                print(curr_node.value, "(tail)")
            else:
                print(curr_node.value, "-> ", end="")

            curr_node = curr_node.next


test_list = SinglyLinkedList()
test_list.insert_end(5)
test_list.insert_end(4)
test_list.insert_end(3)
test_list.print_list()
test_list.insert_end(1)
test_list.insert_end(1)
test_list.insert_end(1)
test_list.print_list()
test_list.remove_at_index(5)
test_list.print_list()