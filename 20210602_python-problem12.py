'''
-Write a function called printSubLists which receives two number A and B as its parameters:

-The function will return the list of all numbers between A and B (A and B not included), 
which are divisible to both 3 and 5. 

'''

def  printSubLists(A, B):
    values = []
    for i in range(A+1, B):
        if i % 3 == 0 and i % 5 == 0:
            values.append(i)
    return values
            
def main():
    
    print(printSubLists(15, 90))
    
main()
