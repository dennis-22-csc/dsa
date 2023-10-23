from singly_linked_list import SinglyLinkedList

def rotate_list(mylist, k):
    current_head = mylist.head_node
    current_node = current_head
    before_last = current_head
    while k:
        while current_node.next_node:
            if current_node.next_node and current_node.next_node.next_node is None:
                before_last = current_node
            current_node = current_node.next_node
        current_node.next_node = current_head
        current_head = current_node
        current_node = current_head
        before_last.next_node = None
        k -= 1
    mylist.head_node = current_head
	

mylist = SinglyLinkedList()
mylist.add_first(1)
#mylist.add_last(2)
#mylist.add_last(3)
#mylist.add_last(4)
#mylist.add(5)

rotate_list(mylist, 1)
for i in mylist:
    print(i)
