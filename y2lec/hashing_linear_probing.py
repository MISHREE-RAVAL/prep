class Dictonary:
    def __init__(self, size):
        self.size = size
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def put(self, key, value):
        hash_value = self.hash_function(key)
        if self.slots[hash_value] is None:
            self.slots[hash_value] = key
            self.data[hash_value] = value
        elif self.slots[hash_value] == key:
            self.data[hash_value] = value
        else:
            new_hash_value = self.rehash(hash_value)
            # Linear probing: continue until slot is empty or key matches
            while self.slots[new_hash_value] is not None and self.slots[new_hash_value] != key:
                new_hash_value = self.rehash(new_hash_value)
            if self.slots[new_hash_value] is None:
                self.slots[new_hash_value] = key
                self.data[new_hash_value] = value
            else:
                self.data[new_hash_value] = value
     
    def __str__(self):
        for i in range(len(self.slots)):
            if self.slots[i] != None:
                print(f"{self.slots[i]}: {self.data[i]}")
 
    def __setitem__(self,key,value):
        self.put(key, value)
        
    def __getitem__(self, key):
        return self.get(key)
        
    def get(self,key):
        start_position = self.hash_function(key)
        current_position = start_position
        
        while self.slots[current_position] != None:
            
            if self.slots[current_position] == key:
                return self.data[current_position]
            
            current_position = self.rehash(current_position)
            
            if current_position == start_position:
                return "not found"

        return "not found"

    def rehash(self, old_hash):
        return (old_hash + 1) % self.size

    def hash_function(self, key):
        return abs(hash(key)) % self.size

D1 = Dictonary(5)
print(D1.slots)
print(D1.data)
D1.put("name", "Alice")
print(D1.slots)
print(D1.data)
D1.put("age", 30)
print(D1.slots)
print(D1.data)
D1.put("name", "Bob")
D1['python']= 56
print(D1.slots)
print(D1.data)
D2 = Dictonary(10)
D2['python'] = 56
D2['java'] = 100
print(D2.get('c'))