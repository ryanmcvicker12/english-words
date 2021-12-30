# MIT License
# Copyright (c) 2017 InnovativeInventor

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

#Ryan McVicker : 27.11.2021
# Usage: python3 scripts/anagram_generator.py
# Example: python3 scripts/anagram_generator.py [TBD]

from pathlib import Path
from random import randint
import os 
import sys
import argparse

#TODO: add support for changing the output file where the words go

#TODO: add support for deciding which letters the user wants to use 
#TODO: add support for windows and macos, currently only works on linux
# 1st command line argument dictates how many characters the word can be 
#TODO: add command line argument to change exactly how many words are generated.



parser = argparse.ArgumentParser()

parser.add_argument('-l','--letters', type = int, help='set the ammount of random letters to be generated.')

parser.add_argument('-n', '--accumulator' ,  type=str, nargs='+', help='an integer for the accumulator', required = False) 




args = parser.parse_args()
print(args) 

def main():
    
    word_list = []

    arguments = sys.argv[1:]

    file_data = ''
    
    #TODO: add argument flags for changing the ammount of letters and other restrictions
    #generate 6 random letters by default

    rand_letters = []

    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    #TODO: add flag for enabling multiple occurences of letters 

    #================== | COMMAND LINE HANDLING | =====================================
    
    #if the user wants to change the letters used for generation
    if args.letters:

            print( args.letters)
        
    #==================================================================================
    #make sure word doesnt have any numbers in it
        
    pattern = ''.join(rand_letters)

    get_words = os.popen(command_string).read().split("\n")
    
    for word in get_words:
        #TODO: eliminate occureces of the same letter 
        if has_numbers(word) != True and len(word) > 2: 
            random_letter_string = ''.join(rand_letters)            
            for letter in word: 
                if word.count(letter) >= random_letter_string.count(letter):
                    word_list.append(word)





    return list(set(word_list)) #remove duplicates
    print(list(set(word_list)))

def has_numbers(inputString):
     return any(char.isdigit() for char in inputString)

if __name__ == '__main__':

   main()
    
