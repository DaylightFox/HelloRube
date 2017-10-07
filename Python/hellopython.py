hw = []
for c in list("Hello World"):
    hw.append(ord(c))

o = []

for i in hw:
    if i == 72:
        o.append(chr(i))
    elif i == 101:
        o.append(chr(i))
    elif i == 108:
        o.append(chr(i))
    elif i == 111:
        o.append(chr(i))
    elif i == 32:
        o.append(chr(i))
    elif i == 87:
        o.append(chr(i))
    elif i == 114:
        o.append(chr(i))
    elif i == 100:
        o.append(chr(i))

print("".join(o))
