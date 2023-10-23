from singly_linked_list import SinglyLinkedList

def swap_nodes(mylist):
	current_node = mylist.head_node
	previous_node = None
	count = 0
	while current_node and current_node.next_node:
		next_node_next_node = current_node.next_node.next_node
		next_node = current_node.next_node
		next_node.next_node = current_node
		current_node.next_node = next_node_next_node
		if previous_node:
			previous_node.next_node = next_node
		count += 1
		if count == 1:
			mylist.head_node = next_node 
		previous_node = current_node
		current_node = next_node_next_node

mylist = SinglyLinkedList()
mylist.add_first(1)
#mylist.add_last(2)
#mylist.add_last(3)
#mylist.add_last(4)
#mylist.add(5)

swap_nodes(mylist)
for i in mylist:
	print(i)
