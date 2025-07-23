class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def traverseAndPrint(head):
    current =head
    while current:
        print(current.data, end="-> ")
        current = current.next
    print("None")
    
def deleteSpecificNode(head,nodeToDelete):
    if head == nodeToDelete:
        return head.next

    current = head
    while current.next and current.next != nodeToDelete:
        current = current.next
    
    if current.next is None:
        return head
    
    current.next = current.next.next
    
    return head

node1 = Node(10)
node2 = Node(20)
node3 = Node(5)
node4 = Node(15)

node1.next = node2
node2.next = node3
node3.next = node4

print('before deletion:')
traverseAndPrint(node1)

node1 = deleteSpecificNode(node1, node3)
print('after deletion:')
traverseAndPrint(node1)
    
