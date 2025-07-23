class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
    def enqueue(self,value):
        new_node = Node(value)

        if self.rear == None:
            self.front = new_node
            self.rear = self.front
        else:
            self.rear.next = new_node
            self.rear = new_node
            
    def dequeue(self):
        if self.front == None:
            return None
        removed_value = self.front.value
        self.front = self.front.next
        return removed_value
       
    def traverse(self):
        
        temp = self.front
        while temp != None:
            print(temp.value, end=' ')
            temp = temp.next
            
    def front_item(self):
        if self.front == None:
            return None
        else:
            return self.front.value
        
    def rear_item(self):
        if self.front == None:
            return None
        else:
            return self.rear.value

q= Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.traverse()
print()
q.dequeue()
q.traverse()
print()
q.front_item()
q.rear_item()
print(q.front_item())
print(q.rear_item())