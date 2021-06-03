'''
-Write a Python function which receives 3 lists as its input parameters and combines 
the lists and remove repeated numbers from the combined list and return the combined list. 
For instance, if the input is [1,2,3,4,2,3] and [3,4,6,7] and [-1,0,23,4] the result is [1,2,3,4,6,7,-1,0,23]

-Note, the order the lists are combined together does not matter.

oSolve this problem using Lists.
oSolve this problem using Sets.

'''

def mixList(list1, list2, list3):
    mixlist = []

    mixlist = set(list1 + list2 + list3)
    return mixlist

def main():

    list1 = [1,2,3,4,2,3]
    list2 = [3,4,6,7]
    list3 = [-1,0,23,4]

    result = mixList(list1, list2, list3)

    print(result)

main()
