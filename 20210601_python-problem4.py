'''
-Write a function which takes no input parameter and allow the user to enter words as many 
as the user wants until the user enters an empty word. When the user enters a word, 
the function will add the word to a list which was originally empty. 
Before the function adds the word to the list, it should check whether 
the same word had been already added to the list or not. If not, 
then the word is added to the list and if yes, the word should not be added to the list. 
The function will eventually return the list of words.

'''

def wordsinput():
    print("Enter words:")
    words=[]
        
    while True:
        word = input("".strip())
                
        if not word:
                break 
        if word not in words:
            words.append(word)
    return words

def main():
    wordslist = wordsinput()
    print(wordslist)
main()
            