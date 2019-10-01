stringg = "Hello world"
listt = [ord(i) for i in stringg]
sett = set(listt)
dic = {}
for i in sett:
    dic.update({i:chr(i)})
for i in listt:
    print(dic[i], end='')
