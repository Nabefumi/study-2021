'''
- Implement a function which receives a list of numbers as an input parameter. The
function will find a sub-list from the list which is sorted and its length is greater than 4
and return the sub-list. If there are more than 1 sub-list, the function can return only one
of them. If there is no such sub-list in the list, the function will return None. 
'''

def findSortedSublist(numbers):
    
    while True:
        if len(numbers) >= 4:
            for size in range(4, len(numbers)):
                for startIndex in range(len(numbers)-size):
                    subList = numbers[startIndex:startIndex+size]
                    if subList == sorted(subList) or subList == sorted(subList, reverse = True):
                        print("Sublist is found", subList)
        
            print("There is no such a subList")
            return None
        else:
            print("There is no such a sublist")
            return None

def main():
    result = findSortedSublist([1,4,5,8,9,6,6,-1,2,6])
main()