#using class stack 

class Stack:
    def __init__(self):
        self.stack = []
        
    def push(self,element):
        self.stack.append(element)
        
    def pop(self):
        if self.isEmpty():
            return "stack is empty"
        return self.stack.pop()
    
    def peek(self):
        if self.isEmpty():
            return "stack is empty"
        return self.stack[-1]
    
    def isEmpty(self):
        return len(self.stack) == 0
    
    def size(self):
        return len(self.stack)
    
    
 
myStack = Stack()

myStack.push('A')
myStack.push('B')
myStack.push('C')

print(myStack.stack)
print(myStack.pop())
print(myStack.stack)
print(myStack.peek())
print(myStack.isEmpty())
print(myStack.size())