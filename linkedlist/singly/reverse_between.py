from singly_linked_list import SinglyLinkedList, Node

def reverse_between(mylist, m, n):
        dummy = Node(0)
        prev = dummy
        dummy.next_node = mylist.head_node 
        #prev = None
        p = mylist.head_node 

        for i in range(1, m):
            prev = p
            print("prev", prev.node_data)
            p = p.next_node
            print("p", p.node_data)

        original_first = p # this is anchor node always pointing to the next-to-be-swapped
        print("original first", original_first.node_data)
        for i in range(m, n):
            current_head = prev.next_node
            print("current head: ", current_head.node_data)
            future_head = original_first.next_node
            print("future head: ", future_head.node_data)
            
            prev.next_node = future_head
            print("prev next node: ", prev.next_node.node_data)
            print("original first", original_first.node_data)
            original_first.next_node = future_head.next_node
            print("original first next node: ", original_first.next_node.node_data)
            future_head.next_node = current_head
            print("future head next node:", future_head.next_node.node_data)
            #break
        mylist.head_node =  dummy.next_node

mylist = SinglyLinkedList()
mylist.add_first(1)
mylist.add_last(2)
mylist.add_last(3)
mylist.add_last(4)
mylist.add(5)

reverse_between(mylist, 1, 4)
for i in mylist:
	print(i)
