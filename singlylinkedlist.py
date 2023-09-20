# Create class Node
class Node:
    def __init__(self, data, next_node):
        self.data = data
        self.next_node = next_node

# Create class SinglyLinkedList
class SinglyLinkedList:
    def __init__(self):
        self.node = None
        self.current_node = None
        self.count = 0

    def add(self, node_data):
        self.count += 1
        if self.count <= 1:
            self.node = Node(node_data, None)
        else:
            self.node = Node(node_data, self.node)

    def add_last(self, node_data):
        self.count += 1
        if self.count <= 1:
            self.node = Node(node_data, None)
        else:
            temp_node = self.node
            # while temp_node.next_node is not None, switch to next node
            while temp_node.next_node:
                temp_node = temp_node.next_node
            # when temp_node.next_node is None, change next_node
            temp_node.next_node = Node(node_data, None)

    def add_at_index(self, node_data, index):
        temp_count = 1
        temp_node = self.node
        if index < 0 or index > self.count:
            raise IndexError("Index out of range")
        while temp_node.next_node:
            if index == 0:
                self.node = Node(node_data, self.node)
                return
            if index == temp_count:
                temp_node.next_node = Node(node_data, temp_node.next_node)
                return
            temp_node = temp_node.next_node
            temp_count += 1
        temp_node.next_node = Node(node_data, temp_node.next_node)

    def delete_at_index(self, index):
        temp_count = 1
        temp_node = self.node
        if index < 0 or index >=self.count:
            raise IndexError("Index out of range")
        while temp_node.next_node:
            if index == 0:
                self.node = self.node.next_node
                return
            if index == temp_count:
                temp_node.next_node = temp_node.next_node.next_node
                return
            temp_node = temp_node.next_node
            temp_count += 1
        temp_node.next_node = temp_node.next_node.next_node

    def __iter__(self):
        self.current_node = self.node
        return self

    def __next__(self):
        if self.current_node is None:
            raise StopIteration

        data = self.current_node.data
        self.current_node = self.current_node.next_node
        return data

    def __getitem__(self, index):
        if index < 0 or index >= self.count:
            raise IndexError("Index out of range")

        current_node = self.node
        for _ in range(index):
            current_node = current_node.next_node

        return current_node.data

# Tester codes
mylist = SinglyLinkedList()
mylist.add(20)
mylist.add(90)
mylist.add(40)
mylist.add(10)
mylist.delete_at_index(0)

# Test that the list is iterable
for i in mylist:
    print(i)

# Test that the list is indexable
#print(mylist[3])

# Test that an index out of range exception will be thrown
#print(mylist[4])
