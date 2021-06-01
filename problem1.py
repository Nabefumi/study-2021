'''

Write a function which take a list of number as an input parameter and find the second
maximum of the list. The second maximum is a number which is bigger than or equal to
all numbers but smaller than the maximum of the list

'''
def findScondMaximum(mylist):
    firstMaximum = max(mylist)
    mylist.remove(firstMaximum)
    while firstMaximum in mylist:
        mylist.remove(firstMaximum)
    
    secondMaximum = max(mylist)
    print("First Maximum is %d and Scond Maximum is %d" %(firstMaximum, secondMaximum))

def main():
    list = [1,2,3,4,5,6,6,7,7,8,8,9,9,]
    findScondMaximum(list)
main()
