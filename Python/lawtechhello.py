hello = ['H', 'e', 'l', 'l', 'o']
world = ['W', 'o', 'r', 'l', 'd', '!']

text = ""

for letter in hello:
    text += letter

text += " "

for letter in world:
    text += letter

print(text)