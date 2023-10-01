class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        

    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            return
        else:
            new_node.next = self.head
            self.head = new_node


    def insert_at_index(self, data, index):
        new_node = Node(data)
        current_node = self.head
        position = 0
        if position == index:
            self.insert_at_beginning(data)
        else:
            while(current_node != None and position + 1 != index):
                position = position + 1
                current_node = current_node.next

            if current_node != None:
                new_node.next = current_node.next
                current_node.next = new_node
            else:
                print("Index not present")

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        
        current_node = self.head
        while(current_node.next):
            current_node = current_node.next
        
        current_node.next = new_node


    def update_node(self, val, index):
        current_node = self.head
        position = 0
        if position == index:
            current_node.data = val
        else:
            while(current_node != None and position != index):
                position = position + 1
                current_node = current_node.next

            if current_node != None:
                current_node.value = val
            else:
                print("Index not present")


    def remove_first_node(self):
        if (self.head == None):
            return
        self.head = self.head.next


    def remove_last_node(self):
        if (self.head == None):
            return
        current_node = self.head
        while(current_node.next.next):
            current_node = current_node.next
        current_node = None
        # current_node = self.head
        # lag_node = self.head
        # while(current_node.next):
        #     lag_node = current_node
        #     current_node = current_node.next
        # lag_node.next = None


    def remove_at_index(self, index):
        if self.head == None:
            return
        
        current_node = self.head
        position = 0

        if index == position:
            self.head = self.head.next
        else:
            while (current_node != None and index != position + 1):
                position = position + 1
                current_node = current_node.next

            if current_node != None:
                current_node.next = current_node.next.next


    def remove_node(self, data):
        current_node = self.head

        while (current_node != None and current_node.next != data):
            current_node = current_node.next
        
        if current_node == None:
            return
        else:
            current_node.next = current_node.next.next

    def print_linked_list(self):
        current_node = self.head
        while(current_node.next):
            print(current_node.data)
            current_node = current_node.next

    def length_of_linked_list(self):
        length = 0
        if (self.head):
            current_node = self.head
            while (current_node):
                length = length + 1
                current_node = current_node.next
            return length
        else:
            return 0


# create a new linked list
llist = LinkedList()
 
# add nodes to the linked list
llist.insert_at_end('a')
llist.insert_at_end('b')
llist.insert_at_beginning('c')
llist.insert_at_end('d')
llist.insert_at_index('g', 2)
 
# print the linked list
print("Node Data")
llist.print_linked_list()
 
# remove a nodes from the linked list
print("\nRemove First Node")
llist.remove_first_node()
print("Remove Last Node")
llist.remove_last_node()
print("Remove Node at Index 1")
llist.remove_at_index(1)
 
 
# print the linked list again
print("\nLinked list after removing a node:")
llist.print_linked_list()
 
print("\nUpdate node Value")
llist.update_node('z', 0)
llist.print_linked_list()
 
print("\nSize of linked list :", end=" ")
print(llist.length_of_linked_list())