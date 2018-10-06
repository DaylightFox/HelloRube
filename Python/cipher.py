word = "Hello World!"
encrypt = ""
s = 5
for alpha in word:
	encrypt += chr(ord(alpha) + s)

decrypt = ""
for alpha in encrypt:
	decrypt += chr(ord(alpha) - s)
print decrypt