'''
Suppose a list of numbers is given.Write a recursive 
function which calculates the Even Factorof a given index of the list.

Even Factor of a given index, i, is the number of numbers in the 
list whose index is lower (smaller) than i.

o Even Factor of index 3 is 1. Because there is only one even number (10) before index 3.
o Even Factor of index 0 is 0. Because there is no even number in the list before index 0.
o Even Factor of index 5 is 2 because there are 2 even numbers (10 and 10) before index 5. 

'''
#Problem4

def evenFactor(nums, index, elementsChecked, total):
    if len(nums) == 0:
        return total
    elif elementsChecked == index:
        return total
    else:
        if nums[0] % 2 == 0:
            total = total + 1
        elementsChecked = elementsChecked + 1
        return evenFactor(nums[1:], index, elementsChecked, total)

#Initializing list
nums=[10,11,15,13,10,1,10,16,20]
index = int(input("Even Factor of index: "))
#Calling recursive function
print("is", evenFactor(nums, index, 0, 0))