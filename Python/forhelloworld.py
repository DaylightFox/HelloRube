#!/usr/bin/python3
### larwal.dev ###

alphabet = ("a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z")

index1 = []
index2 = []
word1 = []
word2 = []

for letter in "hello":
    index1.append(alphabet.index(letter))
for letter in "world":
    index2.append(alphabet.index(letter))

for value in index1:
    word1.append(alphabet[value])
for value in index2:
    word2.append(alphabet[value])  

print (*word1, " ", *word2)
