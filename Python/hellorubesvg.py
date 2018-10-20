# Copyright Henddher Pedroza
# MIT License

art = '''
# # ### #   #   ###    # # ### ##  #   ##
# # #   #   #   # #    # # # # # # #   # #
### ### #   #   # #    # # # # ##  #   # #
# # #   #   #   # #    ### # # # # #   # #
# # ### ### ### ###    # # ### # # ### ##
'''

# 11 characters, 3 pixels wide = 33
# 1 pixel in between chars, 9 in between = 9
# 1/2 pixel on each side (centered)
# 43 pixels
pxlw = 100/43.0
# 5% margin top and bottom
pxlh = 90/5.0

svgrect = '''<rect x="{x}%" y="{y}%" width="{pxlw}%"
height="{pxlh}%" fill="blue" fill-opacity="{fillopacity}"/>'''

svgheader = '''
<!DOCTYPE html>
<html>
<body>
<svg version="1.1"
    baseProfile="full"
    width="600" height="200"
    xmlns="http://www.w3.org/2000/svg">
<rect width="100%" height="100%" fill="red" />

  <!--
  # # ### #   #   ###    # # ### ##  #   ##
  # # #   #   #   # #    # # # # # # #   # #
  ### ### #   #   # #    # # # # ##  #   # #
  # # #   #   #   # #    ### # # # # #   # #
  # # ### ### ### ###    # # ### # # ### ##
  -->

'''
svgfooter = '''

<text x="150" y="125"
    font-size="60" text-anchor="middle" fill="white">SVG</text>
</svg>
</body>
</html>
'''


def emit_rect(i, j, fillopacity):
    print(svgrect.format(
        x=pxlw/2.0+i*pxlw, y=5+j*pxlh,
        pxlw=pxlw, pxlh=pxlh,
        fillopacity=fillopacity))


def gen_rects():
    lines = art.splitlines()
    for j, line in enumerate(filter(lambda l: len(l) != 0, lines)):
        for i, char in enumerate(line):
            if char == ' ':
                fillopacity = '0'
            elif char == '#':
                fillopacity = '1'
            emit_rect(i, j, fillopacity)


if __name__ == '__main__':
    print(svgheader)
    gen_rects()
    print(svgfooter)
