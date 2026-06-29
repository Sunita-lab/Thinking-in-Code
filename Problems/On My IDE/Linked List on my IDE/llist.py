class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    def traverse(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node    

    def delete_at_beginning(self):
        if self.head:
            self.head = self.head.next
        return        

    def delete_at_end(self):
        if not self.head:
            return
        if not self.head.next:
            self.head = None
            return
        second_last = self.head
        while second_last.next.next:
            second_last = second_last.next
        second_last.next = None

    def delete_at_position(self, position):
        if not self.head:
            return
        current = self.head
        target = position - 1
        count = 0
        if position == 0:
            self.head = current.next
            return
        while current and count < target:
            current = current.next
            count += 1
            if not current.next:
                return
        if not current.next:
            return
        current.next = current.next.next  

    def insert_at_position(self, data, position):
        new_node = Node(data)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return
        current = self.head
        count = 0
        while current and count < position - 1:
            current = current.next
            count += 1
        if not current:
            return
        new_node.next = current.next
        current.next = new_node      


llist = LinkedList()

# Insert at end
llist.insert_at_end(10)
llist.insert_at_end(20)
llist.insert_at_end(30)
llist.insert_at_end(40)
print("After insert at end:")
llist.traverse()

# Insert at beginning
llist.insert_at_beginning(5)
print("\nAfter insert at beginning:")
llist.traverse()

# Delete at beginning
llist.delete_at_beginning()
print("\nAfter delete at beginning:")
llist.traverse()

# Delete at end
llist.delete_at_end()
print("\nAfter delete at end:")
llist.traverse()

# Delete at position
llist.delete_at_position(1)
print("\nAfter delete at position 1:")
llist.traverse()    
