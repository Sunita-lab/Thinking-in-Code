class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def traverse(self):
        if not self.head:
            return
        current = self.head
        while True:
            print(current.data)
            current = current.next
            if current == self.head:
                break

    def insert_at_beginning(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = new_node
            return
        current = self.head
        while current.next != self.head:
            current = current.next
        new_node.next = self.head
        current.next = new_node
        self.head = new_node                 

    def delete_at_beginning(self):
        if not self.head:
            return
        if self.head.next == self.head:
            self.head = None
            return
        current = self.head
        while current.next != self.head:
            current = current.next
        current.next = self.head.next
        self.head = self.head.next    

    def delete_at_end(self):
        if not self.head:
            return
        if self.head.next == self.head:
            self.head = None
            return
        current = self.head
        while current.next.next != self.head:
            current = current.next
        current.next = self.head    

    def delete_at_position(self, position):
        if not self.head:
            return
        if position == 0:
            self.delete_at_beginning()
            return
        current = self.head
        count = 0
        while count < position - 1 and current.next != self.head:
            current = current.next
            count += 1
        if current.next == self.head:
            return
        current.next = current.next.next    