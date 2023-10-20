from singly_linked_list import SinglyLinkedList

#count = 0 

def reverse_list_iterative(mylist):
    head = mylist.head_node
    previous, current = None, head
    while current:
        next_node = current.next_node
        current.next_node = previous
        previous = current
        current = next_node
    mylist.head_node = previous

def reverse_list_recursive(mylist):
    def reverse_list(head):
        if not head or not head.next_node:
            return head
        ret = reverse_list(head.next_node)
        head.next_node.next_node = head
        head.next_node = None
        return ret
    ret = reverse_list(mylist.head_node)
    mylist.head_node = ret

mylist = SinglyLinkedList()
mylist.add_first(1)
mylist.add_last(2)
mylist.add_last(3)
mylist.add_last(4)
mylist.add(5)

reverse_list_recursive(mylist)
for i in mylist:
	print(i) 
