class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def traverseAndPrint(head):
    current = head.next
    lowest_value = head.data
    while current:
        if current.data < lowest_value:
            lowest_value =current.data
        current = current.next
    return lowest_value

node1 = Node(10)
node2 = Node(20)
node3 = Node(5)
node4 = Node(15)

node1.next = node2
node2.next = node3
node3.next = node4
print(traverseAndPrint(node1))  # Output should be 5