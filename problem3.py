'''
- Design and implement a function which receives two input parameters 1) a list of integer
numbers and 2) a number. The function will find any occurrence of the given input
number in the list and remove the number from the list and finally will return the new list.

'''

def removeAllOccurrence(numbers, item):
    newList = []
    for element in numbers:
        if element != item:
            newList.append(element)
    return newList

def main():
    result = removeAllOccurrence([1,2,3,4,5,6,0,0,0,5,6,7,8,], 0)
    print(result)
main()