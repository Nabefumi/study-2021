'''
-Write a function which has no input parameter. 
The function ask the user to enter numbers. 
The user can enter repeated numbers but if the user entered a number which was already entered, 
the function will provide an error message to the user and ask the user to enter another one. 
The user can enter numbers as long as s/he has not entered 0. 
Once a 0 is entered, the function returns the sum of all distinct numbers the user had entered. 

'''

def numberinput():
    print("Enter a numbers:")
    numbers=[]
        
    while True:
        number = int(input())
       
        if number == 0:
            break 
        if number not in numbers:
            numbers.append(number)
        elif number in numbers:
            print("%d is alredy in list enter the number" %(number))
    return sum(numbers)

def main():
    numberslist = numberinput()
    print(numberslist)
main()