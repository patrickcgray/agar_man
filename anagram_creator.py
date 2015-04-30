#! /usr/bin/env python3

'''
Created on Apr, 29 2015

@author: Patrick Gray

@summary: Ingest a dictionary text file with one word per line and output a list of anagrams where the
word has >= 4 letters and # of anagrams >= # of letters.

potential optimizations:
-use an list [0-25] as the key value so I can use bucket sort instead of 
'''

import argparse

class AnagramBuilder(object):
    def __init__(self):
        self.anagram_dict = dict()
        pass

    def find_anagrams(self, dictionary_file_name):
        with open(dictionary_file_name) as dictionary_list:
            for word in dictionary_list:
                if len(word) >= 4:
                    word = word.rstrip('\n')
                    #run through every item len > 4 and organize the letters in alphabetical order
                    #then add that item to a hash with a list of items with that same set of characters

                    sorted_character_list = ''.join(sorted(word))
                    
                    if sorted_character_list in self.anagram_dict:
                        self.anagram_dict[sorted_character_list].append(word)
                    else:
                        self.anagram_dict[sorted_character_list] = [word]
                
        #then after reaching the last character iterate through the hash (dict) and print all groups with >= 4 words
        for key, anagram_list in self.anagram_dict.items():
            if len(anagram_list) >= len(key):
                print(', '.join(anagram_list))


def parse_args():
    parser = argparse.ArgumentParser(description='Finds and lists anagrams from a dictionary file. Assumes dict format is a single word per line.')
    parser.add_argument('--filename', nargs='?', type=str, help="Filename of dictionary file.")
    args = vars(parser.parse_args())

    return (args["filename"])

def main(argv=None):
    filename = parse_args()
    
    anagram_builder = AnagramBuilder()

    anagram_builder.find_anagrams(filename)

if __name__ == "__main__":
    main()
