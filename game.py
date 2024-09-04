"""
This is a simple Hangman game using Python programming language. Beginners can use this as a small project to boost their programming skills and understanding logic.

1. The Hangman program randomly selects a secret word from a list of secret words. The random module will provide this ability, so line 1 in program imports it.
2. **The Game:** Here, a random word (a fruit name) is picked up from our collection and the player gets limited chances to win the game.
3. When a letter in that word is guessed correctly, that letter position in the word is made visible. In this way, all letters of the word are to be guessed before all the chances are over.
4. For convenience, we have given length of word + 2 chances. For example, word to be guessed is mango, then user gets 5 + 2 = 7 chances, as mango is a five-letter word.
"""

import random # for random choices
from collections import Counter # for countin number of letters in word

someWords = """apple banana mango strawberry 
orange grape pineapple apricot lemon coconut watermelon 
cherry papaya berry peach lychee muskmelon"""

someWords = someWords.split(' ')
word = random.choice(someWords) # for  random choices

if __name__ == "__main__":
    print("Guess the word. HINT: the word is a fruit.")
    
    letterGuessed = ''
    chances = len(word) + 2
    correct = 0
    flag = 0
    
    for i in word:
        print("_",  end=" ") # by default print function has an in built \n so to avoid it end is used due to which next print fuction does not start with a new a line
    
    try: # what try basically does is lets you try the code and if error come it goes to exception
        while (chances != 0) and flag == 0:
            print() # basically it breaks the line
            chances -= 1
            
            try:
                guess = str(input('Enter a letter to guess: ')) # str is given just make sure its not digit
                guess = guess.lower() # convert everythong in lower case
            except:
                print("Write single letter only")
                
            if not guess.isalpha():
                    print("write a letter only.")
                    continue
            elif len(guess) > 1:
                    print("Write single letter only")
                    continue
            elif guess in letterGuessed:
                    print("You have already written this letter.")
                    continue
                
                
            if guess in word:
                    k = word.count(guess) # it is to check how many times guess var is coming in word var
                    for _ in range(k): # underscre(_) is used cause we wont use it further although we can use any other var
                        letterGuessed += guess # this will add guess var in letterGuessed as mant times as it occurs in  word var
                        
            for char in word:
                if char in letterGuessed and Counter(word) != Counter(letterGuessed):
                        print(char, end = ' ')
                        correct += 1
                     # what this if statement will do is check if the char var form word is in letterGuessed...if it is it will check whether all the letter in word matches the number of specific letter in letterGuessed irrespective of their order.
                elif char in letterGuessed and Counter(word) == Counter(letterGuessed):
                        print("The word is correct. Its", end=' ')
                        print(word)
                        flag = 1
                        print("Congrats you won!!")
                        break
                    # this elif statement is the winning statement and then it will break the while loop
                else:
                        print('_',end = ' ')    
        
        # if user has already used his chances
        if chances <= 0 and Counter(word) != Counter(letterGuessed):
            print("better luck nest time. The word was", end= ' ')
            print(word)
            
    except KeyboardInterrupt:
        # In Python, KeyboardInterrupt is a built-in exception that occurs when the user interrupts the execution of a program using a keyboard action, typically by pressing Ctrl+C. Handling KeyboardInterrupt is crucial, especially in scenarios where a program involves time-consuming operations or user interactions. In this article, we’ll explore how to catch KeyboardInterrupt in Python.
        
        print()
        print("\nBye! try again")
        exit()