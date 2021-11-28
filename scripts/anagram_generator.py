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

#TODO: add support for changing the output file where the words go

#TODO: add support for deciding which letters the user wants to use 
#TODO: add support for windows and macos, currently only works on linux
# 1st command line argument dictates how many characters the word can be 
#TODO: add command line argument to change exactly how many words are generated.
def main():
    
    word_list = []

    arguments = sys.argv[1:]

    file_data = ''
    
    with open(os.path.dirname(__file__) + '/../words.txt') as f:
        file_data = f.read()

    #TODO: add argument flags for changing the ammount of letters and other restrictions
    #generate 6 random letters by default

    rand_letters = []

    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    #TODO: add flag for enabling multiple occurences of letters 
     
    for x in range(0, 5):
        rand_letters.append(alphabet[randint(0, len(alphabet) - 1)])

    #make sure word doesnt have any numbers in it
        
    #find word with the given letters : LINUX ONLY
    pattern = ''.join(rand_letters)

    command_string = "grep -v '[^{}]' words.txt".format(pattern)
    print("command string : " + command_string)
    print("random letters: " + ''.join(rand_letters))

    get_words = os.popen(command_string).read().split("\n")
    
    for word in get_words:
        
        if has_numbers(word) != True and len(word) > 2: 

            #add to the word list to be returned 
            print("word : " +  word)
            word_list.append(word)
    print(word_list)             

def has_numbers(inputString):
     return any(char.isdigit() for char in inputString)

if __name__ == '__main__':

   main()
    
