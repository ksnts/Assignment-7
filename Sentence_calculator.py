#program will get the inputted string/sentence
int1 = input("Input a sentence: ")
#variables 
word1 =0
vowel1 =0
cons1 =0

#for loop and if else to identify string vowel and consonant
#lower() to store the string in lower case in case user inputs upper case letters
for index in int1.lower():
    #increments for counting
    if index in 'aeiou':
        vowel1+=1
    elif index in 'bcdfghjklmnpqrstvwxyz': 
        cons1+=1
#len() for identifying length of string and split() to separate the string and identify the spaces
word1 = len(int1.split())
#output
print("\n")
print(f"{word1} Word(s)")
print(f"{vowel1} Vowel(s)")
print(f"{cons1} Consonant(s)")

        