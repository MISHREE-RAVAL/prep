#linklist

class Node:
    
    def __init__(self,value):
        self.data  = value
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        self.n = 0
        
    def __len__(self):
        return self.n
    
    def insert_head(self,value):
        new_node = Node(value)
        
        new_node.next = self.head
        
        self.head = new_node
        self.n += 1
        print(new_node.data)
    
    #traverse  
    def __str__(self):
        
        curr = self.head
        
        result = ""
        while curr!=None:
            result = result + str(curr.data) + '->'
            curr = curr.next
        return result[:-2]
    
    def append(self,value):
       
        new_node =Node(value)
       
        if self.head == Node:
            self.head = new_node 
            self.n = self.n + 1
            return
         
        curr = self.head
        
        while curr.next != None:
            curr = curr.next
        
        curr.next = new_node
        self.n = self.n + 1
        
    def insert_after(self,after,value):
            
        new_node = Node(value)
            
        curr = self.head
            
        while curr != None:
            if curr.data == after:
                break
            curr = curr.next
        #case 1 break u get item
        if curr != None:
            new_node.next = curr.next
            curr.next = new_node
        else:
            return 'item not found'  
        #case2 loop run full u dont find curr
        
    def clear(self):
        self.head = None
        self.n = 0
    
    def delete_head(self):
        
        if self.head == None:
            return "empty list"
        
        self.head = self.head.next
        self.n = self.n - 1
        
    def pop(self):
        
        if self.head == None:
            return "empty list"
        
        curr = self.head
        
        if curr.next == None:
            return self.delete_head()
        
        while curr.next.next != None:
            curr = curr.next 
           
        curr.next = None
        self.n = self.n - 1 
        
    def remove(self,value):
        
        if self.head == None:
            return "empty link list"
        
        if self.head.data == value:
            return self.delete_head()
        
        curr = self.head
        
        while curr.next != None:
            if curr.next.data == value:
                break
            curr = curr.next
            
        # 2 cases we get value
        # item not get
        if curr.next == None:
            return "item found"
        
        else:
            curr.next = curr.next.next
            
    def search(self,item):
        
        curr = self.head
        pos = 0
        
        while curr != None:
            if curr.data == item:
                return pos
            curr = curr.next
            pos = pos+1
            
        return "not found"
    
    def __getitem__(self,index):
        
        curr = self.head
        pos = 0
        
        while curr != None:
            if pos == index :
                 print(curr.data)
            curr = curr.next
            pos = pos + 1
            return "not in index"
            
            
        
            
    
                   
                    
                    
    
a = Node(1)
b = Node(2)
c = Node(3)

a.next = b
b.next = c

print(a.data)
print(b.data)
print(c.data)
print(a.next)
print(b.next)
print(c.next)

print(id(a))
print(id(b))
print(id(c))

print(int(3616603051280))

#creating linklist
L = LinkedList()
print(L)

#length
print("length of the list is ",len(L))

#insert head
L.insert_head(7)
L.insert_head(4)
L.insert_head(5)
print("hii")

print("length of the list is ",len(L))
print(L)

L.append(5)
print("after appending element at last position",L)
L.insert_after(4,200)
print(L)
L.clear()
print("after clearing list list is empty",L)
print("insering new data")

L.insert_head(7)
L.insert_head(4)
L.insert_head(5)

print("delteing head",L.delete_head())
print(L)
print("pop opn on list",L.pop())
print(L)
print("insering new data")

L.insert_head(7)
L.insert_head(4)
L.insert_head(5)
print("removing 5")
L.remove(5)
print(L)
print("searching opn",L.search(7))

print("index searching",L[1])
print("index searching",L[5])
