import random
from collections import Counter
somewords="apple banana mango strawbaerry orange grape pineapple apricot lemon coconut watermelon cherry papaya berry peach lychee muskmelon"
somewords=somewords.split(" ")
word=random.choice(somewords)
if __name__=="__main__":
    print ("guess the word !hint :word is afruit .")
    for _ in word:
        print("_",end=" ")
    print()
    letterguessed=""
    chances=len (word)+2
    flag=0
    try:
        while chances>0 and flag ==0:
            print()
            chances-=1
            try:
                guess=input("enter a letter to guess:").lower()
            except:
                print ("enter only a letter!")
                continue
            if not guess.isalpha():
                print ("enter only a letter!")
                continue
            elif len(guess)>1:
                print("enter only a single letter!")
                continue
            elif guess in letterguessed:
                print ("you already guessed that letter!")
                continue
            if guess in word:
                letterguessed+=guess*word.count(guess)
            for char in word:
                if char in letterguessed:
                    print (char ,end=" ")
                else:
                    print ("_",end=" ")
            if Counter(letterguessed) == Counter(word):
                print("\nCongratulations! You guessed the word:", word)
                flag = 1
                break

        if chances <= 0 and Counter(letterguessed) != Counter(word):
            print('\nYou lost! The word was:', word)

    except KeyboardInterrupt:
        print ("\ngame interrupted.bye!")
        exit()
        
    