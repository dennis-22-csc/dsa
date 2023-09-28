class Node:
    def __init__(self, node_data, next_node=None):
        self.node_data = node_data
        self.next_node = next_node

class SinglyLinkedList:
    def __init__(self):
        self.head_node = None
        self.count = 0
    def add_last(self, data):
        if not self.head_node:
            new_node = Node(data)
            self.head_node = new_node
            self.count += 1
            return
        temp_node = self.head_node
        new_node = Node(data, temp_node)
        self.head_node = new_node
        self.count += 1
    def add_first(self, data):
        if not self.head_node:
            new_node = Node(data)
            self.head_node = new_node
            self.count += 1
            return
        new_node = Node(data)
        temp_node = self.head_node
        while temp_node.next_node:
            temp_node = temp_node.next_node
        temp_node.next_node = new_node
        self.count += 1
    def add_at_index(self, data, index):
        count = 1
        temp_node = self.head_node
        if index > self.count:
            raise IndexError("Index out of range")
        if index == 0:
            new_node = Node(data, temp_node)
            self.head_node = new_node
            self.count += 1
            return
        while temp_node.next_node:
            if count == index:
                new_node = Node(data, temp_node.next_node)
                temp_node.next_node = new_node
                self.count += 1
                return
            temp_node = temp_node.next_node
            count += 1
        new_node = Node(data, temp_node.next_node)
        temp_node.next_node = new_node
        self.count += 1
    def delete_at_index(self, index):
        count = 1
        temp_node = self.head_node
        if index >= self.count:
            raise IndexError("Index out of range")
        if index == 0:
            self.head_node = temp_node.next_node
            return
        while temp_node.next_node:
            if count == index:
                temp_node.next_node = temp_node.next_node.next_node
                return
            temp_node = temp_node.next_node
            count += 1

    def __iter__(self):
        return self
    def __next__(self):
        if not self.head_node:
            raise StopIteration
        data = self.head_node.node_data
        self.head_node = self.head_node.next_node
        return data

# Tester codes
mylist = SinglyLinkedList()
mylist.add_first(20)
mylist.add_first(90)
mylist.add_first(40)
mylist.add_first(10)
#mylist.delete_at_index(0)
mylist.delete_at_index(3)
#mylist.delete_at_index(4)
for i in mylist:
    print(i)
