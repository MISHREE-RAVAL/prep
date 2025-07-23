import ctypes
class MeraList:
    def __init__(self):
        self.size = 1
        self.n =0
        #create a c type array with size = self.size
        self.A =  self.__make_array(self.size)
        
    def __make_array(self,capacity):
        #creates a c type array(static,referential) with sizecapacity
            return (capacity * ctypes.py_object)()
        
    def __len__(self):
        return  self.n
    
    def append(self,item):
        if self.size == self.n:
            #resize
            self.__resize(self.size*2)
        
        #append
        self.A[self.n] =item
        self.n = self.n+1
        
    def __resize(self,new_capacity):
        #create a new array with new capacity
        B = self.__make_array(new_capacity)
        self.size = new_capacity
        #copy the content of A to B
        for i in range(self.n):
            B[i] = self.A[i]  
        #reassign A
        self.A = B     
       
    #printing    
    def __str__(self):
        #[1,2,3]
        result = ''
        for i in range(self.n):
            result = result + str(self.A[i]) + ','
        return '[' + result[:-1] + ']'
    
    def __getitem__(self,index):
        if 0<= index < self.n:
            return self.A[index]
        else:
            return 'index out of range'   
    
    def pop(self):
        if self.n == 0:
            return 'empty list'
        print(self.A[self.n-1])
        self.n = self.n - 1
        
    def clear(self):
        self.n = 0
        self.size = 1
        
    def find(self,item):
        
        for i in range(self.n):
            if self.A[i] == item:
                return i
        return 'Value not in list'
    
    def insert(self,pos,item):
        if self.n == self.size:
            self.__resize(self.size*2)
        for i in range(self.n,pos,-1):
            self.A[i] = self.A[i-1]
            
        self.A[pos] = item
        self.n = self.n + 1
        
    def __delitem__(self,pos):
        #delete
        if self.n == 0:
            return 'empty list'
        for i in range(pos,self.n-1):
            self.A[i] = self.A[i+1]
        self.n = self.n - 1
        
    def remove(self,item):
        pos = self.find(item)
        
        if type(pos) == int:
            self.__delitem__(pos)
        else:
            return pos
        
        
        
L = MeraList()#making list
print(len(L))#len func
L.append("hello")#append
L.append(3.4)
L.append(True)
L.append(100)
print(len(L))#marking change in len after appending len in item

print(L)
print(L[0])
print(L[7])#out of index

#pop
L.pop()
print(L)

#clear
L.clear()
print(L)

L.append("hello")#append
L.append(3.4)
L.append(True)
L.append(100)
print(L)

#find
print(L.find(3.4))
print(L.find(300))

#insert
L.insert(0,"hii")
print(L)

#delete
del L[3]
print(L)

#remove
L.remove("hii")
print(L)