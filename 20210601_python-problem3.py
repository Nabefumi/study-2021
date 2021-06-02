'''
-Write a function with one input parameter which is a number called size. 
The function then asks the user to enter as many words as the size. 
Then the function will find the followings and returns it as a tuple:

-The first item in the tuple is the size
-The second item in the tuple is the number of words whose length is lessthan 5
-The third item in the tuple is the number of words which only contains upper case letters.
-The fourth item in the tuples is the number of words which contains at least one letter in the word
'''

def word(size):

    lessthanfive = 0
    
    upper = 0
    
    atleastoneletter = 0
    
    for i in range(size):
        word = input("Please input word: ")
        
        if len(word) < 5:
            lessthanfive = lessthanfive +1

        if word.isupper():
            upper = upper +1
        
        for letter in word:
            
            if letter.isalpha():
                atleastoneletter = atleastoneletter +1
                break
    return (size, lessthanfive, upper, atleastoneletter)

def main():
    
    result = word(5)
    print(result)

main()
            
            
    
    
    
    