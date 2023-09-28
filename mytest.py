class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularSinglyLinkedList:
    def __init__(self):
        self.head = None
        self.current = None
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.head.next = self.head
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head

    def __iter__(self):
        self.current = self.head
        return self

    def __next__(self):
        if not self.current:
            raise StopIteration

        data = self.current.data
        self.current = self.current.next

        # Check if we have iterated through all elements
        if self.current == self.head:
            self.current = None

        return data

# Example usage:
if __name__ == "__main__":
    cll = CircularSinglyLinkedList()
    cll.append(1)
    cll.append(2)
    cll.append(3)

    for item in cll:
        print(item)

