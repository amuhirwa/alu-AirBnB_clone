class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def insert(self, prev, value):
        curr = self.head
        node = Node(value)
        while curr.next is not None:
            if curr.data == prev:
                break
            curr = curr.next
        if curr.next is None:
            print('Value not found')
        else:
            node.next = curr.next
            curr.next = node
    
    def remove_node(self, value):
        curr = self.head
        if curr.data == value:
            self.head = curr.next
            del curr
        else:
            while curr.next.data != value:
                curr = curr.next
            curr.next = curr.next.next
            obj = curr.next
            del obj

    def search(self, value):
        curr = self.head
        while curr is not None:
            if curr.data == value:
                return curr
            curr = curr.next
        return None
    
    
    def __str__(self):
        curr = self.head
        string = ""
        while curr.next is not None:
            string += str(curr.data) + " -> "
            curr = curr.next
        string += str(curr.data)
        return string

linked_list = LinkedList()
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
linked_list.insert(1, 6)
print(linked_list)