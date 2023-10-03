from singly_linked_list import SinglyLinkedList

def sort_list(head_node):
    current_node = head_node
    while current_node:
        min_node = current_node
        next_node = current_node.next_node
        current_node_data = current_node.node_data
        while next_node:
            if next_node.node_data < min_node.node_data:
                min_node = next_node
            next_node = next_node.next_node
        current_node.node_data = min_node.node_data
        min_node.node_data = current_node_data
        current_node = current_node.next_node

def selection_sort(head_node):
    current_node = head_node

    while current_node:
        min_node = current_node
        next_node = current_node.next_node
        # Find the minimum node in the remaining unsorted portion
        while next_node:
            if next_node.node_data < min_node.node_data:
                min_node = next_node
            next_node = next_node.next_node

        # Swap the data of the current node and the minimum node
        current_node.node_data, min_node.node_data = min_node.node_data, current_node.node_data


        current_node = current_node.next_node

mylist = SinglyLinkedList()
mylist.add_first(10)
mylist.add_last(90)
mylist.add_last(20)
mylist.add(40)
#print(mylist.head_node)
#print(mylist.head_node.node_data)
sort_list(mylist.head_node)
#print(mylist.head_node)
#print(mylist.head_node.node_data)

for i in mylist:
    print(i)
