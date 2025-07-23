def bubble_sort(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)-1-i):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
                
    print("output through bubble sort",arr)
    
    
arr= [23,12,34,11,100,56,78]
bubble_sort(arr)

def selection_sort(arr):
    for i in range(len(arr)-1):
        
        min = i
        
        for j in range(i+1,len(arr)):
            
            if arr[j] < arr[min]:
                min = j
            
        arr[i],arr[min] = arr[min],arr[i]
        
    print(arr)
    
selection_sort(arr)


def merge_sort(arr1,arr2):
    
    i = j =0
    
    merged = []
    
    while i < len(arr1) and j < len(arr2):
        
        if arr1[i] < arr2[j]:
            merged.append(arr1[i])
            i+=1
        
        else:
            merged.append(arr2[j])
            j+=1
            
    
    
    while i < len(arr1):
        merged.append(arr1[i])
        i+=1
    
    while j < len(arr2):
        merged.append(arr2[j])
        j+=1
        
    print(merged)
    
    

arr1= [1,2,6]
arr2 = [3,5,7]
merge_sort(arr1,arr2)
    
 
def merge_sort(arr):
    
    if len(arr) == 1:
        return arr
    
    mid = len(arr)//2 
    
    left = arr [:mid]
    right = arr [mid:]
    
    left = merge_sort(left)
    right = merge_sort(right)
    
    return merge_sort(left,right) 