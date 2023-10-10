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

count = 0
def merge_sort(head_node):
    global count
    count += 1
    print("count ", count)
    if head_node:
        print("head ", head_node.node_data)
    else:
        print("head ", head_node)
    if head_node is None or head_node.next_node is None:
        return head_node

    # Divide the linked list into two halves.
    print("calling find middle")
    mid_node = find_middle_node(head_node)
    print("returned find middle")
    print("mid node ", mid_node.node_data)
    mid_node_next = mid_node.next_node
    print("mid node next ", mid_node_next.node_data)
    print("mud node next address", mid_node_next)
    mid_node.next_node = None
    print("calling left merge sort")
    left_head = merge_sort(head_node)
    print("returned left merge sort")
    print("hello")
    if left_head:
        print("left head address", left_head)
        print("left head ", left_head.node_data) 
    else:
        print("left head ", left_head)
    print("calling right merge sort")
    if mid_node_next:
        print("mid node nextie", mid_node_next.node_data)
        print("mid node nextie address", mid_node_next)
    right_head = merge_sort(mid_node_next)
    print("returned right merge sort")
    if right_head:
        print("right head ", right_head.node_data)
    else:
        print("right head ", right_head)
    sorted_head =  merge_sorted(left_head, right_head)
    if sorted_head:
        print("sorted head address", sorted_head)
        print("sorted head", sorted_head.node_data)
    else:
        print("sorted head", sorted_head)
    return sorted_head
def find_middle_node(head_node):
    if not head_node:
        return head_node
    slow_node = head_node
    fast_node = head_node

    while fast_node.next_node and fast_node.next_node.next_node:
        slow_node = slow_node.next_node
        fast_node = fast_node.next_node.next_node

    return slow_node

def merge_sorted(left_head, right_head):
    global count
    count += 1
    print("merge count ", count)
    #print("left head ", left_head.node_data)
    #print("right head ", right_head.node_data)
    #print("left head next", left_head.next_node.node_data)
    #return
    result = None
    if not left_head:
        return right_head
    if not right_head:
        return left_head

    if left_head.node_data <= right_head.node_data:
        print("left head ", left_head.node_data)
        print("right head ", right_head.node_data)
        if left_head.next_node:
            print("left head next node ", left_head.next_node.node_data)
        else:
            print("left head next node", left_head.next_node)
        result = left_head
        result.next_node = merge_sorted(left_head.next_node, right_head)
    else:
        if left_head:
            print("left head ", left_head.node_data)
        else:
            print("left head ", left_head)
        if right_head:
            print("right head ", right_head.node_data)
        else:
            print("right head ", right_head)
        if right_head.next_node:
            print("right head next node ", right_head.next_node.node_data)
        else:
            print("right head next node", right_head.next_node)
        result = right_head
        result.next_node = merge_sorted(left_head, right_head.next_node)

    return result

mylist = SinglyLinkedList()
mylist.add(10)
mylist.add_first(30)
mylist.add_last(50)
mylist.add_last(20)
mylist.add(70)
print("calling merge sort")
new_head = merge_sort(mylist.head_node)
print("returned merge sort")
print_list(new_head)

