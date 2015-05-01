#! /usr/bin/env python

'''
Created on Apr, 29 2015

@author: Patrick Gray
'''

import argparse

class AnagramFinder(object):
    def __init__(self):
        self.anagram_dict = dict()
        pass

    def find_anagrams(self, dictionary_file_name):
        with open(dictionary_file_name) as dictionary_list:
            #run through every word in the dictionary where word length is > 4
            for word in dictionary_list:
                word = word.rstrip('\n')                
                if len(word) >= 4:
                    #sort characters in the word to have a consistent way to compare if words are anagrams
                    sorted_character_list = ''.join(sorted(word))

                    #add that word to a hash with the value being a list of words that are anagrams and the key being the alphabetic sorted characters
                    if sorted_character_list in self.anagram_dict:
                        self.anagram_dict[sorted_character_list].append(word)
                    else:
                        self.anagram_dict[sorted_character_list] = [word]

    def print_anagrams(self):
        #iterate through the hash (dict) and print all groups with where # of words >= # of letters in each word
        for key, anagram_list in self.anagram_dict.items():
            if len(anagram_list) >= len(key):
                print(', '.join(anagram_list))


def parse_args():
    parser = argparse.ArgumentParser(description='Finds and lists anagrams from a dictionary file. Assumes dict format is a single word per line.')
    parser.add_argument('--dict_fn', nargs='?', type=str, help="Filename of dictionary file.")
    args = vars(parser.parse_args())

    return (args["dict_fn"])

def main(argv=None):
    dict_fn = parse_args()
    
    anagram_finder = AnagramFinder()

    anagram_finder.find_anagrams(dict_fn)
    anagram_finder.print_anagrams()

if __name__ == "__main__":
    main()
