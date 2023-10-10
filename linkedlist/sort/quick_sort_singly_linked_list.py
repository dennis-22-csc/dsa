from singly_linked_list import SinglyLinkedList

def quick_sort(head_node):
    count = 0

    # Helper function to partition the list and return the pivot node
    def partition(start, end):
        nonlocal count
        pivot = start
        pivot_data = start.node_data
        left = start
        right = start.next_node

        while right != end:
            if right.node_data < pivot_data:
                #left = left.next_node
                left.node_data, right.node_data = right.node_data, left.node_data
                left = left.next_node
            right = right.next_node

        pivot.node_data, left.node_data = left.node_data, pivot.node_data
        count += 1
        return left

    # Recursive quick sort function
    def quick_sort_recursive(start, end):
        if start != end:
            pivot = partition(start, end)
            quick_sort_recursive(start, pivot)
            quick_sort_recursive(pivot.next_node, end)

    # Call the recursive quick sort function
    quick_sort_recursive(head_node, None)
    print("count: ", count)

def partition(start, end):
    pivot = start
    pivot_data = start.node_data
    left = start
    right = start.next_node

    count = 0
    while right != end:
        count += 1
        if count == 0:
            print("left node initial: node ", left.node_data)
            print("right node initial: node ", right.node_data)
            print("end node: ", end)
            print("pivot address: ", pivot)
            print("pivot data: ", pivot_data)
        if right.node_data < pivot_data:
            left = left.next_node
            if count == 2:
                print("left node modified: node ", left.node_data)
            left.node_data, right.node_data = right.node_data, left.node_data
            if count == 0:
                print("left node data modified: ", left.node_data)
                print("left node address: ", left)
                print("right node data modified: ", right.node_data)
                print("right node address: ", right)
        right = right.next_node
        if count == 0:
            if right:
                print("right node next node: node ", right.node_data)
            else:
                print("right node next node: ", right)
            break
        if count == 0:
            return
        #print("count: ", count)

    pivot.node_data, left.node_data = left.node_data, pivot.node_data
    #print("pivot node modified: node ", pivot.node_data)
    #print("pivot node address: ", pivot)
    #print("left node final: node ", left.node_data)
    #print("left node address: ", left)
    return left

mylist = SinglyLinkedList()
mylist.add_first(40)
mylist.add_last(90)
mylist.add_last(50)
mylist.add(70)

#pivot = partition(mylist.head_node, None)
#print("head node data ", mylist.head_node.node_data)
#print("pivot 1", pivot.node_data)
#print("list 1")
#for i in mylist:
    #print(i)
#pivot = partition(mylist.head_node, pivot)
#print("pivot 2", pivot.node_data)
#print("list 2")
#for i in mylist:
    #print(i)
#pivot = partition(mylist.head_node, pivot)
#quick_sort(mylist.head_node)
#print("pivot 3", pivot.node_data)
#print("list 3")

for i in mylist:
    print(i)
