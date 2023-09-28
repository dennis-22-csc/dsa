:class Node:
    def __init__(self, node_data, previous_node = None, next_node = None):
        self.node_data = node_data
        self.previous_node = previous_node
        self.next_node = next_node

class DoublyLinkedList:
    def __init__(self):
        self.current_node = None
        self.previous_node = None
        self.next_node = None
        self.count = 0

    def add(self, node_data):
        if self.current_node is None:
            new_node = Node(node_data)
            self.current_node = new_node
            self.count += 1
            return
        current_node = self.current_node
        new_node = Node(node_data, previous_node=current_node)
        self.current_node = new_node
        current_node.next_node = self.current_node
        self.count += 1

    def add_last(self, node_data):
        if self.current_node is None:
            self.current_node = Node(node_data)
            self.count += 1
            return
        current_node = self.current_node
        while current_node.previous_node:
            current_node = current_node.previous_node
        new_node = Node(node_data, next_node=current_node)
        current_node.previous_node = new_node
        self.count += 1

    def add_at_index(self, node_data, index):
        count = 1
        current_node = self.current_node
        if index > self.count:
            raise IndexError("Index out of bounds")
        while current_node.previous_node:
            if index == 0:
                new_node = Node(node_data, previous_node=current_node)
                self.current_node = new_node
                self.count += 1
                return
            if count == index:
                new_node = Node(node_data, previous_node=current_node.previous_node, next_node=current_node)
                current_node.previous_node = new_node
                self.count += 1
                return
            current_node = current_node.previous_node
        new_node = Node(node_data)
        current_node.previous_node = new_node

    def delete_at_index(self, index):
        count = 0
        current_node = self.current_node
        if index >= self.count:
            raise IndexError("Index out of range")
        if index == 0:
            self.current_node = current_node.previous_node
            return
        while current_node.previous_node:
            if count == index:
                current_node.previous_node.next_node = current_node.next_node
                current_node.next_node.previous_node = current_node.previous_node
                return
            current_node = current_node.previous_node
            count += 1
        current_node = current_node.next_node
        current_node.previous_node = None

    def __iter__(self):
        return self
    def __next__(self):
        if self.current_node is None:
            raise StopIteration
        node_data = self.current_node.node_data
        self.current_node = self.current_node.previous_node
        return node_data

# Test
mylist = DoublyLinkedList()
mylist.add_last(20)
mylist.add_last(90)
mylist.add_last(40)
mylist.add_last(10)
#mylist.add_at_index(100, 4)
mylist.delete_at_index(4)
for i in mylist:
    print(i)
