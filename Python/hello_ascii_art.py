import requests
import numpy as np 

maxx = 10
fonts = requests.get("http://artii.herokuapp.com/fonts_list")
font_list = np.array(fonts.content.split("\n"))
chose = np.arange(0,400,1)
np.random.shuffle(chose)
selected = font_list[chose[:maxx]]
for font in selected:
	ascif = requests.get("http://artii.herokuapp.com/make?text=Hello world!&font="+font)
	print(ascif.content)
