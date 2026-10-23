from PIL import Image

image = Image.open("apple.jpg")
im = image.convert("1")
px = im.load()

fontSize = 10 # font size = height (in code height = 1.5*font size to account for margins); width = height*0.6
width, height = image.size

chars = [' ', '.', ':', '-', '=', '+', '*', '#', '%', '@', '@'] #chars used for shading
art = [] #the end goal is to create a 2d plain of chars

#basic information
print("image size", im.size)
print("y, x how many px one char represents on the image", int(fontSize*1.5), "X", int(fontSize*0.6))
print("ascii art image in chars", height//int(fontSize*1.5), "X", width//int(fontSize*0.6))

#generates the ascii art
for y in range(height//int(fontSize*1.5)): #navigates the y cordinant
	artLine = [] #one line of the result
	for x in range(width//int(fontSize*0.6)): #makes one line of the result
		whites = 0
		for a in range(int(fontSize*1.5)): #navigates the y cordinant
			for b in range(int(fontSize*0.6)): #navigates the x cordinant
				if px[b+(int(fontSize*0.6)*x), a+(int(fontSize*1.5)*y)] == 255:
					whites += 1;

		artLine.append(chars[int((whites/(int(fontSize*1.5)*int(fontSize*0.6)))*10)])

	art.append(artLine)

for c in art: #print the image
	for d in c:
		print(d, end='')
	print()