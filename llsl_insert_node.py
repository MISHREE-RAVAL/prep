class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def traverseAndPrint(head):
    current = head
    while current is not None:
        print(current.data, end=' ')
        current = current.next
    print("null")  # for a new line after printing all elements
    
def insertNodeAtPostion(head,newNode,postion):
    if postion == 1:
        newNode.next = head
        return newNode
    
    current = head
    for _ in range(postion - 2):
        if current is None:
            break
        current = current.next
    
    newNode.next = current.next
    current.next = newNode
    return head

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

print("Original Linked List:")
traverseAndPrint(node1)
newNode = Node(6)
print("Inserting new node with value 6 at position 3:")
node1 = insertNodeAtPostion(node1, newNode, 3)
traverseAndPrint(node1)