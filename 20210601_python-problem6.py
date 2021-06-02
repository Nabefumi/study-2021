'''
-Write a function which lets the user enter English words. 
The user can keep entering English words as long as the user has not entered the word “exit”. 
Once the user enters “exit” the function will return and print 
the list of all distinct words starts with English alphabets
. Like:A: Ali, apple, ...B: Bob, book... until Z

'''

def wordswrap():
    word_list = []
    print("Enter Words")
    while True: 
        word = input()
        if word.lower() == 'exit':
            final_dict = {}
            for i in set(word_list):
                a = i[0]
                data = set([word.capitalize() for word in word_list if (word.lower()).startswith(a.lower())]) ## Find all words starting with letter
                string = ", ".join(data)
                final_dict[a.upper()] = string

            return list(sorted(final_dict.items()))
        word_list.append(word)
        
def main():
    list_of_unique_words = wordswrap()
    for alphabet,words in list_of_unique_words:
        print(alphabet,": ",words)
        
main()