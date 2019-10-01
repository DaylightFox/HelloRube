import urllib.request, re

#I needed help to accomplish this, so of course, I turned to w3 schools!
response = urllib.request.urlopen('https://www.w3schools.com/python/')
search = response.read().decode('utf-8')

#Then I looked around to see if they had an example...
regex = 'print\((.*)\)'
res = re.search(regex, search).groups()[0]

#I think it works!
print(res)
