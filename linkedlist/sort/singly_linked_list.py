class Node:
    def __init__(self, node_data, next_node=None):
        self.node_data = node_data
        self.next_node = next_node

class SinglyLinkedList:
    def __init__(self):
        self.head_node = None
        self.current_node = None
        self.count = 0

    def add(self, data):
        if not self.head_node:
            new_node = Node(data)
            self.head_node = new_node
            self.count += 1
            return
        self.add_last(data)
        self.count += 1

    def add_first(self, data):
        if not self.head_node:
            self.add(data)
            return
        new_node = Node(data, self.head_node)
        self.head_node = new_node
        self.count += 1

    def add_last(self, data):
        if not self.head_node:
            self.add(data)
            return
        temp_node = self.head_node
        while temp_node.next_node:
            temp_node = temp_node.next_node
        new_node = Node(data)
        temp_node.next_node = new_node
        self.count += 1

    def __iter__(self):
        self.current_node = self.head_node
        return self

    def __next__(self):
        if not self.current_node:
            raise StopIteration
        data = self.current_node.node_data
        self.current_node = self.current_node.next_node
        return data

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
