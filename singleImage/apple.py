# this code takes any image and gives you ascii art of it
# it is created for monospace fonts
#
# this code slices up an image in to chunks of a certain size
# after that it every chunk gets a character
#
# HOW TO USE
# 1. set image file path
# 2. (optional) change chunk size if output is too big or has wrong proportions

from PIL import Image

im = Image.open("apple.jpg") # image file path
image = im.convert('L') # convert to greyscale
px = image.load()

chunkSize = (1, 4) # (x, y) in pixels; sets how big one chunk is
chunkWhite = chunkSize[0]*chunkSize[1]*255 # this value represents a pure white chunk; used in calculating a character for a chunk
imageSize = image.size # pixel size of original image
sizeInChunks = (imageSize[0]//chunkSize[0], imageSize[1]//chunkSize[1]) # (x, y)

chars = [' ', '.', ':', '-', '=', '+', '*', '#', '%', '@', '@'] # shading
art = [] # the end goal is to create a 2d plain of chars
artLine = [] # one line of art array

# basic information
print("image size", imageSize)
print("ascii art image in chars", sizeInChunks)

def isWhite(x, y): # gives the % of how close it is pure white
	whites = 0
	for a in range(chunkSize[1]): # y
		for b in range(chunkSize[0]): # x
			whites += px[b+x, a+y]
	return int(whites/chunkWhite*10)

for y in range(sizeInChunks[1]):
	artLine = []
	for x in range(sizeInChunks[0]):
		artLine.append(chars[isWhite(x*chunkSize[0], y*chunkSize[1])])
	art.append(artLine)

for b in art: # print image
	for c in b:
		print(c, end='')
	print()
