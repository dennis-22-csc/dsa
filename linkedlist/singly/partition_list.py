from singly_linked_list import SinglyLinkedList, Node 

def partition(mylist, x):
    less_head = less_current = Node(0)
    greater_head = greater_current = Node(0)

    current = mylist.head_node

    while current:
        if current.node_data < x:
            less_current.next_node = current
            less_current = less_current.next_node
        else:
            greater_current.next_node = current
            greater_current = greater_current.next_node
        current = current.next_node

    # Connect the two partitions
    less_current.next_node = greater_head.next_node
    greater_current.next_node = None

    # Update the head_node
    mylist.head_node = less_head.next_node

def partition_list(mylist, pivot):
	left_head = Node(mylist.head_node.node_data)
	right_head = Node(mylist.head_node.node_data)
	left_current = left_head
	right_current = right_head
	current_node = mylist.head_node 
	
	while current_node:
		if current_node.node_data < pivot:
			left_current.next_node = current_node
			left_current = left_current.next_node
		else:
			right_current.next_node = current_node
			right_current = right_current.next_node
		current_node = current_node.next_node 

	left_current.next_node = right_head.next_node
	right_current.next_node = None
	mylist.head_node = left_head.next_node
	
mylist = SinglyLinkedList()
mylist.add_first(1)
mylist.add_last(4)
mylist.add_last(3)
mylist.add_last(2)
mylist.add(5)
mylist.add_last(2)

partition_list(mylist, 3)

for i in mylist:
	print(i)
