# Create class Node
class Node:
    def __init__(self, data, next_node):
        self.data = data
        self.next_node = next_node

# Create class SinglyLinkedList
class SinglyLinkedList:
    def __init__(self):
        self.current_node = None
        self.count = 0

    def add(self, node_data):
        self.count += 1
        if self.count <= 1:
            new_node = Node(node_data, None)
            self.current_node = new_node
        else:
            new_node = Node(node_data, self.current_node)
            self.current_node = new_node

    def add_last(self, node_data):
        self.count += 1
        if self.count <= 1:
            new_node = Node(node_data, None)
            self.current_node = new_node
        else:
            current_node = self.current_node
            # while current_node.next_node is not None, switch to next node
            while current_node.next_node:
                current_node = current_node.next_node
            # when current_node.next_node is None, change next_node to new node
            new_node = Node(node_data, None)
            current_node.next_node = new_node

    def add_at_index(self, node_data, index):
        temp_count = 1
        current_node = self.current_node
        if index < 0 or index > self.count:
            raise IndexError("Index out of range")
        while current_node.next_node:
            if index == 0:
                new_node = Node(node_data, self.current_node)
                self.current_node = new_node
                return
            if index == temp_count:
                new_node = Node(node_data, current_node.next_node)
                current_node.next_node = new_node
                return
            current_node = current_node.next_node
            temp_count += 1
        new_node = Node(node_data, current_node.next_node)
        current_node.next_node = new_node

    def delete_at_index(self, index):
        temp_count = 1
        current_node = self.current_node
        if index < 0 or index >=self.count:
            raise IndexError("Index out of range")
        while current_node.next_node:
            if index == 0:
                new_node = self.current_node.next_node
                self.current_node = new_node
                return
            if index == temp_count:
                current_node.next_node = current_node.next_node.next_node
                return
            current_node = current_node.next_node
            temp_count += 1
        current_node.next_node = current_node.next_node.next_node

    def __iter__(self):
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

        current_node = self.current_node
        for _ in range(index):
            current_node = current_node.next_node

        return current_node.data

# Tester codes
mylist = SinglyLinkedList()
mylist.add_last(20)
mylist.add_last(90)
mylist.add_last(40)
mylist.add_last(10)
#mylist.delete_at_index(0)
print(mylist.current_node.data)
# Test that the list is iterable
#for i in mylist:
    #print(i)

# Test that the list is indexable
#print(mylist[3])

# Test that an index out of range exception will be thrown
#print(mylist[4])
