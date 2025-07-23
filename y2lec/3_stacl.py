class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def isempty(self):
        return self.top is None

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node

    def traverse(self):
        temp = self.top
        while temp is not None:
            print(temp.data)
            temp = temp.next

    def peek(self):
        if self.isempty():
            return "stack empty"
        else:
            return self.top.data

    def pop(self):
        if self.isempty():
            return "is empty"
        else:
            popped = self.top.data
            self.top = self.top.next
            return popped

    def size(self):
        count = 0
        temp = self.top
        while temp is not None:
            count += 1
            temp = temp.next
        return count

    def reverse_string(self, text):
        # Clear the stack before use (optional, if you want to reuse the stack)
        while not self.isempty():
            self.pop()
        for i in text:
            self.push(i)
        res = ""
        while not self.isempty():
            res += str(self.pop())
        print(res)
        
    def undo_redo(self, text, pattern):
        u = Stack()
        r = Stack()
        res = ""
        for i in text:
            u.push(i)
        for i in pattern:
            if i == "u":
                data = u.pop()
                if data != "is empty":
                    r.push(data)
            else:
                data = r.pop()
                if data != "is empty":
                    u.push(data)
        while not u.isempty():
            res = u.pop() + res
        print(res)

def find_the_celb(L):
    s = Stack()
    for i in range(len(L)):
        s.push(i)
    while s.size() >= 2:
        i = s.pop()
        j = s.pop()
        if L[i][j] == 0:
            s.push(i)
        else:
            s.push(j)
    if s.isempty():
        print("No celeb found")
        return
    celeb = s.pop()
    for i in range(len(L)):
        if i != celeb:
            if L[i][celeb] == 0 or L[celeb][i] == 1:
                print("No celeb found")
                return
    print("Celebrity is:", celeb)

s = Stack()

print("Is empty:", s.isempty())
s.push(1)
print("Is empty after push:", s.isempty())
s.push(2)
s.push(3)
print("Stack contents:")
s.traverse()
s.pop()
print("After popping one element:")
s.traverse()
print("Reverse string 'hello':")
s.reverse_string("hello")
s.undo_redo("kolkata","uurrurur")
L = [
    [0,0,1,1],
    [0,0,1,0],
    [0,0,0,0],
    [0,0,1,0]
]

find_the_celb(L)