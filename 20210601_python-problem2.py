'''
-Write a function which receives a list and returns True if the list is “Partially sorted” 
and returns False if the list is not “Partially Sorted”. 
A list is “Partially sorted” if and only if there exists an item in the list which if removed, 
the list will become a sorted list. 
For instance the following list is “Partially sorted”:
-[1,2,5,10,6,8,9] This is partially sorted because it is not originally sorted but if we remove 
10 from the list, then the list is sorted. 

'''

def isSorted(list1):
    if list1 == sorted(list1):
        return True
    else:
        return False

def isPartially(list1):
    for i in range(0, len(list1)):
        temp = list1.pop(i)
        numbers =  isSorted(list1)

        if temp == True:
            return True
            break
        else:
            list1.insert(i, temp)
    return False

def main():
    list1 = [1,2,5,10,6,8,9]
    print(isPartially(list1))
main()
        