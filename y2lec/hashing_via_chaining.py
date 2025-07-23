class Node:

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class LL:

    def __init__(self):
        self.head = None

    def add(self, key, value):
        new_node = Node(key, value)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node

    def delete_head(self):
        if self.head is None:
            return "Empty"
        else:
            self.head = self.head.next

    def remove(self, key):
        if self.head is None:
            return "Empty"
        if self.head.key == key:
            self.delete_head()
            return
        temp = self.head
        while temp.next is not None:
            if temp.next.key == key:
                break
            temp = temp.next
        if temp.next is None:
            return "Not Found"
        else:
            temp.next = temp.next.next

    def traverse(self):
        temp = self.head
        while temp is not None:
            print(temp.key, "-->", temp.value, " ", end=" ")
            temp = temp.next
        print()

    def size(self):
        temp = self.head
        counter = 0
        while temp is not None:
            counter += 1
            temp = temp.next
        return counter

    def search(self, key):
        temp = self.head
        pos = 0
        while temp is not None:
            if temp.key == key:
                return pos
            temp = temp.next
            pos += 1
        return -1

    def get_node_at_index(self, index):
        temp = self.head
        counter = 0
        while temp is not None:
            if counter == index:
                return temp
            temp = temp.next
            counter += 1
        return None

class Dictionaary:
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        # creating an array of linked lists
        self.buckets = self.make_array(self.capacity)

    def make_array(self, capacity):
        L = []
        for i in range(capacity):
            L.append(LL())
        return L
    
    def __setitem__(self, key, value):
        self.put(key, value)
        
    def __getitem__(self, key):
        return self.get(key)
    
    def __delitem__(self, key):
        
        bucket_index = self.hash_function(key)
        
        self.buckets[bucket_index].remove(key)
        
    def __str__(self):
        for i in self.buckets:
            i.traverse()
            
        return ""
    
    def __len__(self):
        return self.size
        
    def get(self, key):
        bucket_index = self.hash_function(key)
        
        res = self.buckets[bucket_index].search(key)
        
        if res == -1:
            return -1
        else:
            node = self.buckets[bucket_index].get_node_at_index(res)
            return node.value
        

    def put(self, key, value):
        bucket_index = self.hash_function(key)
        node_index = self.get_node_index(bucket_index, key)
        if node_index == -1:
            self.buckets[bucket_index].add(key, value)
            self.size += 1
            
            load_factor = self.size / self.capacity
            print(f"Load factor: {load_factor}")
            
            if load_factor >=2:
                self.rehash()
        else:
            node = self.buckets[bucket_index].get_node_at_index(node_index)
            node.value = value
            
    def rehash(self):
        self.capacity = self.capacity * 2
        old_buckets = self.buckets
        A = self.buckets
        self.size = 0
        self.buckets = self.make_array(self.capacity)
        
        for i in old_buckets:
            for j in range(i.size()):
                node = i.get_node_at_index(j)
                key_item = node.key
                value_item = node.value
                self.put(key_item, value_item)

    def get_node_index(self, bucket_index, key):
        node_index = self.buckets[bucket_index].search(key)
        return node_index

    def hash_function(self, key):
        return abs(hash(key)) % self.capacity

    def __str__(self):
        result = []
        for i, bucket in enumerate(self.buckets):
            temp = bucket.head
            while temp is not None:
                result.append(f"Bucket {i}: {temp.key} --> {temp.value}")
                temp = temp.next
        return "\n".join(result)

L = LL()
L.add(2, 3)
L.add(4, 5)
L.add(6, 7)
L.traverse()
D1 = Dictionaary(5)
D1.put("name", "Alice")
bucket_index = D1.hash_function("name")
D1.buckets[bucket_index].traverse()
print(D1)
print(D1.get_node_index(bucket_index, "name"))  # Should return the index of the node with key "name"
print(D1.buckets[bucket_index].get_node_at_index(0).value)  # Should print "Alice"
D1.put("name", "Bob")  # Update value for key "name"
D1.put("rubby",20000)
D1.put("java",30000)
D1.put("python",40000)
D1.put("c++",50000)
D1.put("javascript",60000)
D1.put("c#",70000)
D1.put("go",80000)

# Print all buckets and their contents
for i, bucket in enumerate(D1.buckets):
    print(f"Bucket {i}:", end=" ")
    bucket.traverse()
    
D1.put("rubby1",20000)
D1.put("rubby2",20000)
D1.put("rubby3",20000)
D1.put("rubby4",20000)
D1.put("rubby5",20000)

for i, bucket in enumerate(D1.buckets):
    print(f"Bucket {i}:", end=" ")
    bucket.traverse()

print(D1["php"])
print(D1["name"])

del D1["rubby3"]

for i, bucket in enumerate(D1.buckets):
    print(f"Bucket {i}:", end=" ")
    bucket.traverse()
    
print(len(D1))  # Should print the number of items in the dictionary