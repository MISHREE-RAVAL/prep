class Queue:
    def __init__(self):
        self.queue = []
    
    def enqueue(self, element):
        self.queue.append(element)
        
    def dequeue(self):
        if self.isEmpty():
            return "queue is empty"
        return self.queue.pop(0)
    
    def peek(self):
        if self.isEmpty():
            return "queue is empty"
        return self.queue[0]
    
    def isEmpty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)

myQueue = Queue()

myQueue.enqueue(1)
myQueue.enqueue(2)
myQueue.enqueue(3)

print(myQueue.queue)
print(myQueue.peek())
print(myQueue.dequeue())
print(myQueue.queue)
print(myQueue.isEmpty())
print(myQueue.size())