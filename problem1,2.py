'''
#Problem1
Write a recursive function which reverse a string word. You cannot use reverse function of Python. 
You need to design a recursive algorithm and implement it. What is time complexity of your solution?

'''
#problem1
def stringReceive(word):
    if len(word) == 1 or len(word) == 0:
        return 1
    else:
        return word

def main():

    word = input("Please enter a word: ")
    word = stringReceive(word[::-1])
    print(stringReceive(word))
main()

'''
#Problem2
Write e recursive function to check whether a string word whose length is even, is palindromeor not. 
A palindrome word is a word which is equal to its reversed.
'''
#problem2
def isPalindrome(input_string):
    for i in range(len(input_string)):
        if input_string[i] == input_string[-i-1]:
            return True
        else:
            return False

print(isPalindrome("iiiaaaiii"))
print(isPalindrome("aaalllssdfgh"))


    
    
            




