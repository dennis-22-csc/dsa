class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

class CircularSinglyLinkedList:
    def __init__(self):
        self.head_node = None
        self.count = 0

    def add(self, data):
        if not self.head_node:
            new_node = Node(data)
            self.head_node = new_node
            self.count += 1
            return
        self.add(data)

    def add_first(self, data):
        if not self.head_node:
            self.add(data)
            return
        old_head_node = self.head_node
        new_head_node = Node(data, old_head_node)
        self.head_node = new_head_node
        temp_node = old_head_node
        while temp_node.next_node:
            if temp_node.next_node == old_head_node:
                temp_node.next_node = new_head_node
                self.count += 1
                return
            temp_node = temp_node.next_node
        temp_node.next_node = new_head_node
        self.count += 1

    def add_last(self, data):
        if not self.head_node:
            self.add(data)
            return
        temp_node = self.head_node
        while temp_node.next_node:
            if not temp_node.next_node.next_node or temp_node.next_node.next_node == self.head_node:
                new_node = Node(data, self.head_node)
                temp_node.next_node.next_node = new_node
                self.count += 1
                return
            temp_node = temp_node.next_node
        new_node = Node(data, self.head_node)
        temp_node.next_node = new_node
        self.count += 1

    def add_at_index(self, data, index):
        count = 1
        temp_node = self.head_node
        if index > self.count:
            raise IndexError("Index out of range")
        if index == 0:
            self.add_first(data)
            return
        if index == self.count:
            self.add_last(data)
            return
        while temp_node.next_node:
            if count == index:
                new_node = Node(data, temp_node.next_node)
                temp_node.next_node = new_node
                self.count += 1
                return
            temp_node = temp_node.next_node
            count += 1

    def delete_at_index(self, index):
        count = 1
        temp_node = self.head_node
        old_head_node = self.head_node
        if index >= self.count:
            raise IndexError("Index out of range")
        if index == 0:
            self.head_node = temp_node.next_node
        while temp_node.next_node:
            if count == index:
                temp_node.next_node = temp_node.next_node.next_node
                return
            if index == 0 and temp_node.next_node == old_head_node:
                temp_node.next_node = self.head_node
                return
            temp_node = temp_node.next_node
            count += 1

mylist = CircularSinglyLinkedList()
mylist.add_last(20)
mylist.add_last(90)
mylist.add_last(40)
mylist.add_last(10)
mylist.add_at_index(100, 0)
mylist.delete_at_index(0)

node1 = mylist.head_node
node2 = node1.next_node
node3 = node2.next_node
node4 = node3.next_node
node5 = node4.next_node

print(node1.data)
print(node2.data)
print(node3.data)
print(node4.data)
print(node5.data)
