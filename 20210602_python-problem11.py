'''
-Design and implement a functionwhich receives two input parameters 1) 
a list of integer numbers and 2) a number. 
The function will find any occurrence of the given input number in the list and remove 
the number from the list and finally will return the new list.-Hint: Use a list

'''

def removeNumber(listOfNumbers, number):
 
    for i in listOfNumbers:
        if(i == number): 
            listOfNumbers.remove(i) 
    return listOfNumbers 
    
newList = removeNumber([1,2,3,4,5,6,7,8,9,0,1,2,3,1],1)
print("After removing the occurrences of the number, the result is ",newList)