import random
n=0
s=list("Hello world!")
while 1:
    print("try %d" %n)
    n+=1
    random.shuffle(s)
    if "".join(s)=="Hello world!":
        print("".join(s))
        break
    
