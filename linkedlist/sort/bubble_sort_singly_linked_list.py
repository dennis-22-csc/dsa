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

    def sort_data(self):
        swapped = True
        while swapped:
            swapped = False
            temp_node = self.head_node
            while temp_node.next_node:
                next_node = temp_node.next_node
                next_node_data = next_node.node_data
                temp_node_data = temp_node.node_data
                if temp_node_data > next_node_data:
                    temp_node.node_data = next_node_data
                    next_node.node_data = temp_node_data
                    swapped = True
                temp_node = temp_node.next_node

    def sort_node(self):
        swapped = True
        while swapped:
            swapped = False
            current_node = self.head_node
            previous_node = None
            while current_node and current_node.next_node:
                next_node = current_node.next_node
                current_node_data = current_node.node_data
                next_node_data = next_node.node_data
                if current_node_data > next_node_data:
                    if not previous_node:
                        self.head_node = next_node
                    else:
                        previous_node.next_node = current_node.next_node
                    current_node.next_node = current_node.next_node.next_node
                    next_node.next_node = current_node
                    swapped = True
                previous_node = current_node
                current_node = current_node.next_node

mylist = SinglyLinkedList()
mylist.add_first(90)
mylist.add_last(40)
mylist.add_last(20)
mylist.add(10)
#print(mylist.head_node)
#print(mylist.head_node.node_data)
mylist.sort_node()
#print(mylist.head_node)
#print(mylist.head_node.node_data)
for i in mylist:
    print(i)
