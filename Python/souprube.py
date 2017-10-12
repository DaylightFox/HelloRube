import urllib2
import requests 
from bs4 import BeautifulSoup
from random import *

hello_rube_markup = urllib2.urlopen("http://github.com").read()
hello_rube_soup = BeautifulSoup(hello_rube_markup, "html.parser")
hello_rube_soup = str(hello_rube_soup)

hello_count = 0
goal = "hello world"
is_printing = False


for char in range(len(hello_rube_soup)):
	
	if hello_rube_soup[char] == goal[hello_count]:
		print hello_rube_soup[char],
		is_printing = True
		hello_count=hello_count+1
		if hello_rube_soup[char] == goal[len(goal)-1]:
			break
	elif hello_count < 8 and char == hello_rube_soup[len(hello_rube_soup)-1]:
		for remaining_index in range(hello_count, 8):
			print goal[remaining_index],
			break
	elif is_printing==False and char==hello_rube_soup[len(hello_rube_soup)-1]:
		print goal
		break
