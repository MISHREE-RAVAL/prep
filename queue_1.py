queue = []

queue.append(1)
queue.append(2)
queue.append(3)

#peek
first = queue[0]
print("first",first)

#dequeue
dequeued = queue.pop(0)
print("dequeued",dequeued)

print("queue after dequeue", queue)

#isempty
isEmpty = not bool(queue)
print("isEmpty",isEmpty)

#size
size = len(queue)
print("size", size)
