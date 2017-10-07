#! python3
# helloinputworld.py - Takes user input and gives the impression that calculations are preformed to turn it into "Hello World"

import time

#ask for user input that will appear to convert to hello world
answer = ""
while answer == "":
    answer = input("Type in any word or phrase:")
answer = answer.split()

#take their input and show status messages that give the impression that input is being adjusted 
if len(answer) < 2:
    for i in answer:
        print("Converting " + i + " to Hello")
        time.sleep(.5)
        print("Converted")
        time.sleep(.5)
        print("Adding World! to answer")
        time.sleep(.5)
        print("Added!")
        time.sleep(.5)
        answer = "Hello World!"
else:
    for i,c in enumerate(answer):
        if i < 1:
            print("Converting " + c + " to Hello")
            time.sleep(.5)
            print("Converted")
            time.sleep(.5)
        elif i == 1:
            print("Converting " + c + " to World!")
            time.sleep(.5)
            print("Converted")
            time.sleep(.5)
        else:
            print("Deleting " + c)
            time.sleep(.5)
    answer = "Hello World"
time.sleep(.5)
print("Your new answer is " + answer)
