#stack using linked list
class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        
class Stack:
    def __init__(self):
        self.head = None
        self.size = 0
        
    def push(self, value):
        new_node = Node(value)
        if self.head:
            new_node.next = self.head
        self.head = new_node
        self.size+=1
        
    def pop(self):
        if self.isEmpty():
            return "stack is empty"
        popped_value = self.head
        self.head = self.head.next
        self.size -= 1
        return popped_value.value
    
    def peek(self):
        if self.isEmpty():
            return "stack is empty"
        return self.head.value
    
    def isEmpty(self):
        return self.head is None

    def get_size(self):
        return self.size            
    
    def traverseAndPrint(self):
        current = self.head
        while current:
            print(current.value, end="-> ")
            current = current.next
        print()




myStack = Stack()
myStack.push('A')
myStack.push('B')
myStack.push('C')

print("linkedlist:",end="")
myStack.traverseAndPrint()
print("peek",myStack.peek())
print("pop",myStack.pop())
print("linkedlist after pop", end="")
myStack.traverseAndPrint()
print("isEmpty",myStack.isEmpty())
print("size",myStack.get_size())