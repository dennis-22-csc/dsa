class Node:
    def __init__(self, data, previous_node=None, next_node=None):
        self.data = data
        self.previous_node = previous_node
        self.next_node = next_node

class DoublyLinkedList:
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

    def add_first(self, data):
        if not self.head_node:
            self.add(data)
            return
        old_head_node = self.head_node
        new_head_node = Node(data, next_node=old_head_node)
        old_head_node.previous_node = new_head_node
        self.head_node = new_head_node
        self.count += 1

    def add_last(self, data):
        if not self.head_node:
            self.add(data)
            return
        temp_node = self.head_node
        while temp_node.next_node:
            temp_node = temp_node.next_node
        old_tail_node = temp_node
        new_tail_node = Node(data, previous_node=old_tail_node)
        old_tail_node.next_node = new_tail_node
        self.count += 1

    def add_at_index(self, data, index):
        if not self.head_node:
            self.add(data)
            return
        if index == 0:
            self.add_first(data)
            return
        if index == self.count:
            self.add_last(data)
            return
        if index > self.count:
            raise IndexError("Index out of range")
        count = 1
        temp_node = self.head_node
        while temp_node.next_node:
            if count == index:
                new_node = Node(data, previous_node=temp_node, next_node=temp_node.next_node)
                temp_node.next_node = new_node
                self.count += 1
                return
            temp_node = temp_node.next_node
            count += 1

    def delete_at_index(self, index):
        if index == 0:
            self.head_node = self.head_node.next_node
            self.head_node.previous_node = None
            self.count -= 1
            return
        if index > self.count:
            raise IndexError("Index out of bounds")
        count = 1
        temp_node = self.head_node
        while temp_node.next_node:
            if index == count and index != self.count - 1:
                temp_node.next_node = temp_node.next_node.next_node
                temp_node.next_node.previous_node = temp_node
                self.count -= 1
                return
            temp_node = temp_node.next_node
            count += 1
        temp_node = temp_node.previous_node
        temp_node.next_node = None
        self.count -= 1

    def __iter__(self):
        self.current_node = self.head_node
        return self

    def __next__(self):
        if not self.current_node:
            raise StopIteration
        data = self.current_node.data
        self.current_node = self.current_node.next_node
        return data

mylist = DoublyLinkedList()
mylist.add(90)
mylist.add_first(20)
mylist.add_last(40)
mylist.add(10)
mylist.add_at_index(100, 2)
mylist.add_at_index(200, 0)
mylist.add_at_index(300, 6)
#mylist.add_at_index(400, 8)
mylist.delete_at_index(2) # 90
mylist.delete_at_index(0) # 200
mylist.delete_at_index(4) # 300
#mylist.delete_at_index(5)

for i in mylist:
    print(i)
