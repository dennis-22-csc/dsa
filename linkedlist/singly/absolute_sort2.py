from singly_linked_list import SinglyLinkedList, Node

def sort_linked_list_by_absolute_in_place(head_node):
    current_node = head_node

    while current_node is not None:
        next_node = current_node.next_node

        if next_node and abs(next_node.node_data) < abs(current_node.node_data):
            # Swap the nodes if the next node's absolute value is smaller
            temp_data = current_node.node_data
            current_node.node_data = next_node.node_data
            next_node.node_data = temp_data

            # Start from the beginning of the list to recheck ordering
            current_node = head_node
        else:
            current_node = next_node

linked_list = SinglyLinkedList()
linked_list.add(10)
linked_list.add(5)
linked_list.add(-10)
linked_list.add(0)
linked_list.add(-5)
linked_list.add(2)

sort_linked_list_by_absolute_in_place(linked_list.head_node)

for data in linked_list:
    print(data)


