'''
Write a function which receives a list and returns a number. 
In the list, all numbers have been repeated twice except one number that is repeated once. 
The function should return the number that is repeated once and return it

'''

def returnDuplicateOnce(numbers):
    
    for i in numbers:

        if numbers.count(i) == 2:
            return None
        return i
  
def main():
    numbers = [1,24,24,6,3,6,3,6,3]
    print(returnDuplicateOnce(numbers))
main()
