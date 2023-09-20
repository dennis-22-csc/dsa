class Node:
    def __init__(self, node_data, previous_node = None, next_node = None):
        self.node_data = node_data
        self.previous_node = previous_node
        self.next_node = next_node

class DoublyLinkedList:
    def __init__(self):
        self.current_node = None
        self.previous_node = None
        self.next_node = None

    def add(self, node_data):
        if self.current_node is None:
            self.current_node = Node(node_data)
            return
        temp_node = self.current_node
        self.current_node = Node(node_data, temp_node)
        temp_node.next_node = self.current_node

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
mylist.add(20)
mylist.add(90)
mylist.add(40)
mylist.add(10)

for i in mylist:
    print(i)
