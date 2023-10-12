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
    
def find_middle_node(head_node):
	slow_node = head_node
	fast_node = head_node
	while fast_node.next_node and fast_node.next_node.next_node:
		slow_node = slow_node.next_node
		fast_node = fast_node.next_node.next_node
	return slow_node
	
def get_new_right(right_head):
	current_node = right_head
	previous_node = None
	while current_node:
		temp_node = current_node.next_node
		current_node.next_node = previous_node
		previous_node = current_node
		current_node = temp_node
	return previous_node
	
def order_halves(left_head, right_head):
	left = left_head
	right = right_head
	while right:
		next_node_left = left.next_node
		next_node_right = right.next_node
		left.next_node = right
		right.next_node = next_node_left
		left = next_node_left
		right = next_node_right
	
def order_list(head_node):
    mid_node = find_middle_node(head_node)
    mid_node_next = mid_node.next_node
    mid_node.next_node = None
    left_head = head_node
    right_head = get_new_right(mid_node_next)
    order_halves(left_head, right_head)
    
	
mylist = SinglyLinkedList()
mylist.add_first(1)
mylist.add_last(2)
mylist.add_last(3)
mylist.add_last(4)
mylist.add(5)

order_list(mylist.head_node)
for i in mylist:
	print(i)
