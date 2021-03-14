#!/bin/python3

import math
import os
import random
import re
import sys


class Node:
    def __init__(self):
        self.children = {}
        self.end = False
        
def insert(word,index,trie,is_prefix):
    
    if trie.end == True: #if prefix is found
        is_prefix = True
        
    if index == len(word):
        trie.end = True
        for key in trie.children: #if prefix comes after its parent(a string holds the prefix) is added to the trie
            return True
        return is_prefix
    
    if word[index] not in trie.children: #add to trie
        trie.children[word[index]] = Node()
        
    return insert(word,index + 1,trie.children[word[index]],is_prefix)

def noPrefix(words):
    
    trie = Node()
    is_prefix = False
    
    for word in words:
        res = insert(word,0,trie,is_prefix)
        if res:
            print("BAD SET")
            print(word)
            return
        
    print("GOOD SET")

    

if __name__ == '__main__':
    n = int(input().strip())

    words = []

    for _ in range(n):
        words_item = input()
        words.append(words_item)

    noPrefix(words)
