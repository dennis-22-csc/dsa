class Node:
    def __init__(self, node_data, next_node=None):
        self.node_data = node_data
        self.next_node = next_node

class CircularSinglyLinkedList:
    def __init__(self):
        self.current_node = None
        self.next_node = None
        self.head_node = None
        self.count = 0

    def add(self, node_data):
        if self.count == 0:
            new_node = Node(node_data)
            self.current_node = new_node
            self.count += 1
            return
        if self.count == 1:
            current_node = self.current_node
            new_node = Node(node_data, current_node)
            current_node.next_node = new_node
            self.current_node = new_node
            self.count += 1
            return
        current_node = self.current_node
        new_node = Node(node_data, current_node.next_node)
        current_node.next_node = new_node
        self.current_node = new_node
        self.count += 1

    def __iter__(self):
        self.head_node = self.current_node
        return self

    def __next__(self):
        if not self.head_node:
            raise StopIteration

        node_data = self.current_node.node_data
        self.current_node = self.current_node.next_node

        if self.head_node == self.current_node:
            self.head_node = None

        return node_data


# Tester codes
mylist = CircularSinglyLinkedList()
mylist.add(20)
mylist.add(90)
mylist.add(40)
mylist.add(10)

for i in mylist:
    print(i)
