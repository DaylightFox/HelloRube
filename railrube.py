hello = "Hello World"
helloRail = []
for r in range(3):
    helloRail.append([])
    for c in range(len(hello)):
        helloRail[r].append(".")
r = 0
down = True
for c,char in enumerate(hello):
    helloRail[r][c] = char
    r += 1 if down else -1
    if r == 2:
        down = False
    elif r == 0:
        down = True
for r in helloRail:
    print(r)
