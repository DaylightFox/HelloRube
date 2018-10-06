###By silvericarus
import sys
from random import randint

### arraystitch(array)
### Takes an array and returns a string sesulting
### of concatenating all the elements of the array
def arraystitch(array):
  result = ""
  for element in array:
    result = result + str(element)
  
  return result

### lettergen(obj)
### Takes a letter as an objective and generates random
### ASCII codes for letters until they match, then returns it
def lettergen(obj):
  letter = str(chr(randint(65,122)))
  while letter!=str(obj):
    letter = str(chr(randint(65,122)))
  
  return letter

def main(argv):
  helloworld = []
  word1 = "Hello"
  for letter in word1: 
    helloworld.append(lettergen(letter))

  helloworld.append(" ")

  word2 = "world"
  for letter in word2: 
    helloworld.append(lettergen(letter))

  print(str(arraystitch(helloworld))+str(chr(33)))

if __name__ == "__main__":
    main(sys.argv)
