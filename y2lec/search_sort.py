#linear sort o(n) it's brute force

import time
import random


def linear_search(arr,item):
    
    for i in range(len(arr)):
        if arr[i] == item:
            return i
    return -1

arr = [12,34,56,1,67,100,47,99]

print(linear_search(arr,121))
print(linear_search(arr,56))

def binary_search(arr,low,high,item):
    
    if low <= high:
        
        mid = (low+high)//2
        
        if arr[mid] == item:
            return mid
        
        elif arr[mid] > item:
            return binary_search(arr,low,mid-1,item)
        else:
            return binary_search(arr,mid+1,high,item)
    
    else:
        return -1
    
arr = [12,34,47,56,67,99,100,]
    
print(binary_search(arr,0,len(arr)-1,47))

def is_sorted(arr):
    
    sorted = True
    
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            sorted = False
    return sorted

def monkey_sort(arr):
    
    while not is_sorted(arr):
        time.sleep(1)
        random.shuffle(arr)
        print(arr)
    print(arr)

arr = [10,5,76]
monkey_sort(arr)




a=[1,2,3,4]
random.shuffle(a)
print(a)