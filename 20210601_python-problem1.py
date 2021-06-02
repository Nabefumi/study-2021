'''

-Implement a function which receives a list and returns True 
if the list is already sorted ascendingly and returns 0 if the list is not sorted ascendingly.
oSolve this problem once using the Sort function
oSolve this problem once without using the Sort function

'''

def isSortesd(numbers):
    
    if len(numbers) == 0 or len(numbers) == 1:
        return True
    
    for i in range(1, len(numbers)):
        if numbers[i -1] > numbers[i]:
            return 0
    return True

def main():
    arr1 = [1,3,5,6,2,4]
    print(isSortesd(arr1))
    arr2 = [1,2,3,4,5,6]
    print(isSortesd(arr2))
    
main()
    