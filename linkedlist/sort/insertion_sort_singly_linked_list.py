def c_print(text):
    with open('stdout', 'a') as file:
        file.write(f"{text}\n")

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
    def sort_list(self):
        sorted_list = SinglyLinkedList()
        current_node_main = self.head_node

        while current_node_main:
            previous_node = None
            current_node_sorted = sorted_list.head_node

            next_node_main = current_node_main.next_node

            while current_node_sorted and current_node_main.node_data > current_node_sorted.node_data:
                previous_node = current_node_sorted
                current_node_sorted = current_node_sorted.next_node
            if not previous_node:
                current_node_main.next_node = sorted_list.head_node
                sorted_list.head_node = current_node_main
            else:
                previous_node.next_node = current_node_main
                current_node_main.next_node = current_node_sorted

            current_node_main = next_node_main
        self.head_node = sorted_list.head_node

    def insertion_sort(self):
        if self.head_node is None or self.head_node.next_node is None:
            return

        # Initialize a new linked list to store the sorted nodes
        sorted_list = SinglyLinkedList()

        current_node = self.head_node
        count = 0
        while current_node:
            count += 1
            next_node = current_node.next_node  # Save the next node before removing

            # Find the correct position to insert the current node in the sorted list
            sorted_node = sorted_list.head_node
            prev_node = None

            c_print(f"Iteration: {count}")

            c_print(f"current node: {current_node.node_data}")

            if next_node:
                c_print(f"next_node: {next_node.node_data}")
            else:
                c_print(f"next_node: {next_node}")

            if sorted_node:
                c_print(f"sorted_node: {sorted_node.node_data}")
            else:
                c_print(f"sorted_node: {sorted_node}")

            while sorted_node and sorted_node.node_data < current_node.node_data:
                prev_node = sorted_node
                sorted_node = sorted_node.next_node
                if count == 4:
                    c_print(f"inner_prev_node: {prev_node.node_data}")
                    c_print(f"inner_sorted_node: {sorted_node.node_data}")
            if prev_node:
                c_print(f"new_prev_node: {prev_node.node_data}")
            else:
                c_print(f"new_prev_node: {prev_node}")
            if sorted_node:
                c_print(f"new_sorted_node: {sorted_node.node_data}")
            else:
                c_print(f"new_sorted_node: {sorted_node}")
            if count == 4:
                return
            # Insert the current node into the sorted list
            if prev_node is None:
                current_node.next_node = sorted_list.head_node
                sorted_list.head_node = current_node
            else:
                prev_node.next_node = current_node
                current_node.next_node = sorted_node

            if prev_node:
                if prev_node.next_node:
                    c_print(f"prev_node.next_node: {prev_node.next_node.node_data}")
                else:
                    c_print(f"prev_node.next_node: {prev_node.next_node}")
            if current_node.next_node:
                c_print(f"current_node.next_node: {current_node.next_node.node_data}")
            else:
                c_print(f"current_node.next_node: {current_node.next_node}")
            if sorted_list.head_node:
                c_print(f"sorted_list.head_node: {sorted_list.head_node.node_data}")
            else:
                c_print(f"sorted_list.head_node: {sorted_list.head_node}")


            # Move to the next node in the original list
            current_node = next_node

        # Replace the original list with the sorted list
        self.head_node = sorted_list.head_node

mylist = SinglyLinkedList()
mylist.add_first(10)
mylist.add_last(90)
mylist.add_last(20)
mylist.add(40)
#print(mylist.head_node)
#print(mylist.head_node.node_data)
mylist.sort_list()
#print(mylist.head_node)
#print(mylist.head_node.node_data)

for i in mylist:
    print(i)
