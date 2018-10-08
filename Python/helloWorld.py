# -*- coding: utf-8 -*-
"""
Created on Sat Oct  6 23:01:16 2018

@author: biome
"""


class HelloWorld:
    alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
    def __init__(self):
        flag = False
        word = "hello world"
        for w in word:
            if w == " ":
                print(' ', end='')
            if w in self.alphabets: 
                    self.printAlphabet(self.alphabets.index(w))        
        
    def printAlphabet(self, index):
            print(self.alphabets[index], end='')
            
            
hello = HelloWorld()

        
