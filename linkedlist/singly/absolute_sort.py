from singly_linked_list import SinglyLinkedList

def print_list(head):
    if head is None:
        print(' ')
        return
    curr_node = head
    while curr_node:
        print(curr_node.node_data, end = " ")
        curr_node = curr_node.next_node
    print(' ')

def absolute_sort(head_node):
    current_node = head_node.next_node 
    previous_node = head_node
    while current_node:
	    if current_node.node_data < 0:
		    current_next = current_node.next_node
		    current_node.next_node = head_node 
		    head_node = current_node
		    previous_node.next_node = current_next
		    current_node = current_next
	    else:
		    previous_node = current_node
		    current_node = current_node.next_node
    return head_node		
		
mylist = SinglyLinkedList()
mylist.add_first(0)
mylist.add_last(2)
mylist.add_last(-5)
mylist.add_last(5)
mylist.add(10)
mylist.add(-10)

new_head = absolute_sort(mylist.head_node)
print_list(new_head)
