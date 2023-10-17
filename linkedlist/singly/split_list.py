from singly_linked_list import SinglyLinkedList, Node 

def print_linked_list_parts(result):
    for sublist in result:
        current = sublist
        print("[", end="")
        while current:
            print(current.node_data, end="")
            current = current.next_node
            if current:
                print(", ", end="")
        print("]")

def splitListToParts(root, k):
        counts = 0
        each = root
        while each:
            counts += 1
            each = each.next_node
        num = counts // k
        rem = counts % k
        nodes = []
        for i in range(k):
            head = Node(0)
            each = head
            #print("root 1", root.node_data)
            for j in range(num):
                node = Node(root.node_data)
                #print("root", root.node_data)
                each.next_node = node
                each = each.next_node
                root = root.next_node
            if rem:
                rmnode = Node(root.node_data)
                each.next_node = rmnode
                if root.next_node:
                    root = root.next_node
                rem -= 1
            nodes.append(head.next_node)
        return nodes
        
mylist = SinglyLinkedList()
mylist.add_first(1)
mylist.add_last(2)
mylist.add_last(3)
mylist.add_last(4)
#mylist.add(5)

splitted_list = splitListToParts(mylist.head_node, 2)
print_linked_list_parts(splitted_list)

#mylist.add(6)
#mylist.add(7)
#mylist.add(8)
#mylist.add(9)
#mylist.add(10)

#splitted_list = split_list(mylist.head_node, 3)
#print_linked_list_parts(splitted_list)

