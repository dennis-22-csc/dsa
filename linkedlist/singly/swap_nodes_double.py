from singly_linked_list import SinglyLinkedList

def swap_nodes_double(mylist, k):
        res = [] 
        
        curr = mylist.head_node 
        while curr:
            res.append(curr)
            curr = curr.next_node
        
        res[k-1].node_data, res[-k].node_data = res[-k].node_data, res[k-1].node_data

def swap_nodes(mylist, k):
    head = mylist.head_node
    if not head:
        return head

    # Find the kth node from the beginning
    kth_from_beginning = head
    count = 1
    current = head
    while current:
        if count == k:
            kth_from_beginning = current
        current = current.next_node
        count += 1

    # Find the kth node from the end
    kth_from_end = head
    current = kth_from_beginning
    while current.next_node:
        current = current.next_node
        kth_from_end = kth_from_end.next_node

    # Swap the values
    kth_from_beginning.node_data, kth_from_end.node_data = kth_from_end.node_data, kth_from_beginning.node_data
    
   # 7,9,6,6,7,8,3,0,9,5
mylist = SinglyLinkedList()
mylist.add_first(7)
mylist.add_last(9)
mylist.add_last(6)
mylist.add_last(6)
mylist.add(7)
mylist.add_last(8)
mylist.add_last(3)
mylist.add_last(0)
mylist.add_last(9)
mylist.add_last(5)
#swap_nodes_double(mylist, 2)
swap_nodes(mylist, 5)
for i in mylist:
	print(i)
