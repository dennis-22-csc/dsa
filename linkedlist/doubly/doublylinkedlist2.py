class Node:
    def __init__(self, data, previous_node=None, next_node=None):
        self.data = data
        self.previous_node = previous_node
        self.next_node = next_node

class DoublyLinkedList:
    def __init__(self):
        self.head_node = None
        self.current_node = None
        self.forward = None
    def add_last(self, data):
        self.forward = False
        if not self.head_node:
            new_node = Node(data)
            self.head_node = new_node
            return
        temp_node = self.head_node
        new_node = Node(data, previous_node=temp_node)
        temp_node.next_node = new_node
        self.head_node = new_node
    def add_first(self, data):
        self.forward = True
        if not self.head_node:
            new_node = Node(data)
            self.head_node = new_node
            return
        temp_node = self.head_node
        while temp_node.next_node:
            temp_node = temp_node.next_node
        new_node = Node(data, previous_node=temp_node)
        temp_node.next_node = new_node
    def __iter__(self):
        self.current_node = self.head_node
        return self
    def __next__(self):
        if self.current_node is None:
            raise StopIteration
        data = self.current_node.data
        if self.forward:
            self.current_node = self.current_node.next_node
        else:
            self.current_node = self.current_node.previous_node
        return data


# Tester codes
mylist = DoublyLinkedList()
mylist.add_last(20)
mylist.add_last(90)
mylist.add_last(40)
mylist.add_last(10)

for i in mylist:
    print(i)
