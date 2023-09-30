class Node:
    def __init__(self, data, previous_node=None, next_node=None):
        self.data = data
        self.previous_node = previous_node
        self.next_node = next_node
        
class CircularDoublyLinkedList:
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

        temp_node = self.head_node

        while temp_node.next_node:
            if temp_node.next_node == self.head_node:
                break
            temp_node = temp_node.next_node
        old_head_node = self.head_node
        new_head_node = Node(data, previous_node=temp_node, next_node=old_head_node)
        old_head_node.previous_node = new_head_node
        temp_node.next_node = new_head_node
        self.head_node = new_head_node
        self.count += 1

    def add_last(self, data):
        if not self.head_node:
            self.add(data)
            return
        temp_node = self.head_node
        while temp_node.next_node:
            if temp_node.next_node == self.head_node:
                new_node = Node(data, previous_node=temp_node, next_node=self.head_node)
                temp_node.next_node = new_node
                self.head_node.previous_node = new_node
                self.count += 1
                return
            temp_node = temp_node.next_node
        new_node = Node(data, previous_node=temp_node, next_node=self.head_node)
        temp_node.next_node = new_node
        self.head_node.previous_node = new_node
        self.count += 1

    def add_at_index(self, data, index):
        if not self.head_node:
            self.add(data)
            return
        count = 1
        temp_node = self.head_node
        if index == 0:
            self.add_first(data)
            return
        if index == self.count:
            self.add_last(data)
            return
        if index > self.count:
            raise IndexError("Index out of bounds")
        while temp_node.next_node:
            if count == index:
                new_node = Node(data, previous_node=temp_node, next_node=temp_node.next_node)
                temp_node.next_node.previous_node = new_node
                temp_node.next_node = new_node
                self.count += 1
                return
            temp_node = temp_node.next_node
            count += 1

    def delete_at_index(self, index):
        count = 1
        temp_node = self.head_node
        if index >= self.count:
            raise IndexError("Index out of range")
        while temp_node.next_node:
            if count == index:
                temp_node.next_node.next_node.previous_node = temp_node
                temp_node.next_node = temp_node.next_node.next_node
                return
            if index == 0 and temp_node.next_node == self.head_node:
                new_head_node = self.head_node.next_node
                new_head_node.previous_node = temp_node
                temp_node.next_node = new_head_node
                self.head_node = new_head_node
                return
            temp_node = temp_node.next_node
            count += 1

    def __iter__(self):
        self.current_node = self.head_node
        return self

    def __next__(self):
        if not self.current_node:
            raise StopIteration
        data = self.current_node.data
        self.current_node = self.current_node.next_node
        if self.current_node == self.head_node:
            self.current_node = None
        return data
# Tester codes
mylist = CircularDoublyLinkedList()
mylist.add_last(20)
mylist.add_last(90)
mylist.add_last(40)
mylist.add_last(10)
mylist.delete_at_index(4)

# Next node
node1 = mylist.head_node
node2 = node1.next_node
node3 = node2.next_node
node4 = node3.next_node
#node5 = node4.next_node

# Previous node
node6 = node4.previous_node
node7 = node6.previous_node
node8 = node7.previous_node
#node9 = node8.previous_node
#node10 = node9.previous_node

print("From Beginning")
print(node1.data)
print(node2.data)
print(node3.data)
#print(node4.data)
#print(node5.data)

print("From end")
print(node6.data)
print(node7.data)
print(node8.data)
#print(node9.data)
#print(node10.data)
