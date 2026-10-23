from PIL import Image

image = Image.open("apple.jpg")
im = image.convert("1")
px = im.load()

fontSize = 10 # font size = height; width = height*0.6
width, height = image.size
charHeight = int(fontSize*1.5) 
charWidth  = int(fontSize*0.6)
artHeight  = height//charHeight
artWidth   = width//charWidth

chars = [' ', '.', ':', '-', '=', '+', '*', '#', '%', '@', '@']
art = [] #the end goal is to create a 2d plain of chars

#basic information
print("image size", im.size)
print("y, x how many px one char represents on the image", charHeight, "X", charWidth)
print("ascii art image in chars", artHeight, "X", artWidth)

def isWhite(x, y): #gives the % of white pixels in an area represented by one char
	whites = 0
	for a in range(charHeight): #navigates the y cordinant
		for b in range(charWidth): #navigates the x cordinant
			if px[b+x, a+y] == 255:
				whites += 1;
	return (whites/(charHeight*charWidth))*10 #returns percentage

#generates the ascii art
for y in range(artHeight): #navigates the y cordinant
	artLine = [] #one line of the result
	for x in range(artWidth): #makes one line of the result
		artLine.append(chars[int(isWhite(x*charWidth, y*charHeight))])

	art.append(artLine)

for b in art: #print the image
	for c in b:
		print(c, end='')
	print()
