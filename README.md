###Agar Man: Anagram Finder

####Summary:
This program will:

1.  Ingest a "dictionary" text file with one word per line

2.  Output a list of anagrams contained in the input file if:

  a.  (# of letters in the word) >= 4

  b.  (# of anagrams in the group) >= (# of letters in the word)

####Usage:

```
./anagram_finder.py --dict_fn <filename> 
```

This assumes python 2.7 or greater is installed on the system.

###Testing:

For the included test case ```test_input.txt```

Output should be:
```
hello, heoll, llheo, lhleo, olleh
ascot, coast, costa, tacso, tasco
emir, mire, reim, riem, rime
yaas, aasy, saay, ayas
```

####Assumptions:

-assuming that all words are in the dictionary - does not find external anagrams

-assuming that output order doesn't matter - neither within anagram groups nor for the groups of anagrams themselves

-assuming no repeated words

####Potential Optimizations:
-use an list [0-25] as the key value so I can use bucket sort instead of default python Timsort

-testing should be automated
