"""
Given a list of words, group the words that are anagrams of each other. 
(An anagram are words made up of the same letters).

Example:

Input: ['abc', 'bcd', 'cba', 'cbd', 'efg']
Output: [['abc', 'cba'], ['bcd', 'cbd'], ['efg']]

Here's a starting point:

import collections

def groupAnagramWords(strs):
  # Fill this in.

print groupAnagramWords(['abc', 'bcd', 'cba', 'cbd', 'efg'])
# [['efg'], ['bcd', 'cbd'], ['abc', 'cba']]
"""
import collections

def groupAnagramWords(strs):
    # Fill this in.
    words_dict = collections.defaultdict(list)
    result=[]

    for i in strs:
        # x ia list that stores components of i
        # x --> sorted component
        x= sorted(i)
        # y converts list --> str
        y=''.join(x)
        # add i into the key -> sorted component(y)
        words_dict[y].append(i)
    
    # add the words_dict element into result list
    # but it adds from the first item of words_dict into last item of result
    for i in words_dict.values():
        result.append(i)

    # need to reverse sequence
    return result[::-1]

print (groupAnagramWords(['abc', 'bcd', 'cba', 'cbd', 'efg']))
# [['efg'], ['bcd', 'cbd'], ['abc', 'cba']]