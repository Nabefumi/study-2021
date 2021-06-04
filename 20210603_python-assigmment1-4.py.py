'''
Problem1
Implement a function which receives a list of numbers as its input parameter and apply 
Selection sort on and sort the list and return it. 

'''

def sellect_sort(arr):
    for ind, ele in enumerate(arr):
        min_ind = min(range(ind, len(arr)), key=arr.__getitem__)
        arr[ind], arr[min_ind] = arr[min_ind], ele
    return arr
    
'''
Problem2
Implement a function which receives a list of numbers as its input parameter and apply 
Mergesort on and sort the list and return it.

'''
   
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)


def merge(left, right):
    merged = []
    l_i, r_i = 0, 0

    while l_i < len(left) and r_i < len(right):
        if left[l_i] <= right[r_i]:
            merged.append(left[l_i])
            l_i += 1
        else:
            merged.append(right[r_i])
            r_i += 1

    if l_i < len(left):
        merged.extend(left[l_i:])
    if r_i < len(right):
        merged.extend(right[r_i:])
    return merged
    
'''
Problem3
Implement a function which receives a list of numbers and a number as its input 
parameters and apply Linear search to check whetherthe given number is inside the 
given list or not. The function will return the index of the number in the list if the number 
exists in the list or will return -1 if the number does not exist in the list.

'''
def linearSearch(arr):
    
    i = 0
    n = len(arr)
    target = input("Please enter the search number: ")
    
    while i < n:
        if arr[i] == target:
            return i
        i += 1
    return -1
    
'''
Problem4
Similar to Problem 3, Implement a function which receives a list of 
numbers and a number as its input parameters and apply Binarysearch 
to check whetherthe given number is inside the given list or not. 

The function will return the index of the number in the list if the number
exists in the list or will return -1 if the number does not exist in the list.
'''
def binarySearch(arr):
    target = input("Please enter the search number: ")
    n = len(arr)
    left = 0
    right = n -1
    
    while left <= right:
        center = (left + right) // 2
        if arr[center] == target:
            return center
        elif arr[center] < target:
            left = center +1
        else:
            right = center +1
    return -1
    print("Not finded number")

def main():
    inputnum = input("Please enter a numbers: ")
    arr = list(inputnum)
    #Problem1
    result1 = sellect_sort(arr)
    print(result1)
    
    #Problem2
    result2 = merge_sort(arr)
    print(result2)
    
    #Problem3
    result3 = linearSearch(arr)
    print("position: {}.".format(result3))
    
    #Problem4
    result4 = binarySearch(arr)
    print("position: {}.".format(result4))

main()

    
