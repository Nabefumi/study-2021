'''
-Design and implement a function which has one input parameter which is a number 
which is greater than 50, called num. Then the function will create a dictionary whose 
keys are 2 and 3 and 4 and 5 and 6 and 7 and 8 and 9. 
Then the function calculates the values for each of the above keys. 
The value for a key is all the numbers between 2 and input “num” that are divisible by the key. 
The function eventually will print the result. 

-Hint: Use a dictionary whose values are lists.
-Example:num = 20
2: [2,4,6,8,10,12,14,16,18,20]
3: [3,6,9,12,15,18]
4: [4,8,12,16,20]
5: [5,10,15,20]
6: [6,12,18]
7: [7, 14]
8: [8, 16]
9: [9, 18]

'''

def findNum(num):
    result = dict()
    for i in range(2,10):
        numbers = []
        for j in range(2,num+1):
            if j % i == 0:
                numbers.append(j)
        result[str(i)] = numbers

    for key in result:
        print(key,":",result[key])

findNum(20)
        