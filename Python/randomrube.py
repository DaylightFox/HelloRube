# Let's hope you're lucky!
# 33-111 is the ASCII values for space to "o", 78 possibilities
# "Hello World!" has length of 12
# Odds: 12^78 ~= 1.5 x 10^84

import random

world = "Hello World!"
word = ""


while (word!=world):
	word = ""
	for c in range(len(world)):
		word+=chr(random.randint(33,111))

print word

