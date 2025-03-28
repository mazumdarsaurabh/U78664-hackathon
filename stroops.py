from .charecterMap import count_char
from .countWords import count_word
from .getPermute import permut
from .makeTitle import make_title
from .normalizeSpaces import normalize
from .removePunctuation import remove_Punctuation
from .reverse_word import reverse_words
from .substring_find import spansub
from .transform import transformm
 
def plaGame():
    print("................................Go For what you need .................................")
    print("1.getspan(s, ss) 2.reverseWords(s) 3.removePunctuation(s) 4.countWords(s) \n 5.charecterMap(s) "
    "6.makeTitle(s) 7.normalizeSpaces(s) 8.transform(s) 9.getPermutations(s) 10.exit" )
 
    while True:
        print("1.getspan(s, ss) 2.reverseWords(s) 3.removePunctuation(s) 4.countWords(s) \n 5.charecterMap(s) "
            "6.makeTitle(s) 7.normalizeSpaces(s) 8.transform(s) 9.getPermutations(s) 10.exit" )
        p=int(input(" please select the number : "))
 
        if p==1:
            strr = input("enter the string: ")
            sub_str = input("enter the substring: ")
            print(spansub(strr,sub_str))
        elif p==2:
            print (reverse_words(input("Enter the word : ")))
 
        elif p==3:
            print (remove_Punctuation(input("Enter the word : ")))
 
        elif p==4:
            print (count_word(input("Enter the word : ")))
       
        elif p==5:
            print (count_char(input("Enter the word : ")))
 
        elif p==6:
            print (make_title(input("Enter the word : ")))
 
        elif p==7:
            print (normalize(input("Enter the word : ")))
 
        elif p==8:
            print (transformm(input("Enter the word : ")))
 
        elif p==9:
            print (permut(input("Enter the word : ")))
 
        elif p==10:
            break
 
plaGame()
 
 
 