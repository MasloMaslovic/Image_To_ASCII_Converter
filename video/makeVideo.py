# this code creates a text file full of ascii art images from a video file
# it is created for monocpace fonts
#
# this code slices up a frame in to chunks of a certain size and gives every chunk a character
# after that it records the characters in to a text file
#
# HOW TO USE
# 1. set video file path
# 2. play the video with playVideo.py (generated text file required)
# 3. (optional) chenge chunk size if output is too big or has wrong proportions
# 4. play the video with playVideo.py (generated text file required)

import cv2

video = cv2.VideoCapture("bad_apple.mp4") # omage file path
out = open("bad_apple.txt", "a") # open text file in append mode

chunkSize = (2, 5) # (x, y) in pixels; sets how big one chunk is
chunkWhite = chunkSize[0]*chunkSize[1]*255 # this value represents a pure white chunk; used in calculating a character for a chunk
imageSize = (int(video.get(cv2.CAP_PROP_FRAME_WIDTH)), int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))) # (x, y) pixel size of original image
sizeInChunks = (imageSize[0]//chunkSize[0], imageSize[1]//chunkSize[1]) # (x, y)

chars = [' ', '.', ':', '-', '=', '+', '*', '#', '%', '@', '@']
art = [] # the end goal is to create a 2d plain of chars (single frame)
artLine = [] # one line of art array

frameCount = 0 # set up frame counter

def isWhite(x, y, px): # gives the % of how close it is pure white
	whites = 0
	for a in range(chunkSize[1]): # y
		for b in range(chunkSize[0]): # x
			whites += int(px[a+y, b+x])
	return int((whites/chunkWhite)*10)

# basic information
print("start")
print("size", imageSize)
print("ascii art image in chars", sizeInChunks)

while True:
	ret, frameOG = video.read() # load new frame
	if not ret: # break if new frame not available
		print("no more frames")
		break
	frame = cv2.cvtColor(frameOG, cv2.COLOR_BGR2GRAY) # convert image to grayscale

	art = [] # reset art array

	for y in range(sizeInChunks[1]):
		artLine = []
		for x in range(sizeInChunks[0]):
			artLine.append(chars[isWhite(x*chunkSize[0], y*chunkSize[1], frame)])
		art.append(artLine)

	for c in art: # print ascii art to file
		for d in c:
			out.write(str(d))
		out.write('\n')
	out.write(";\n") # separate frames

	frameCount += 1
	if frameCount%100 == 0: # helps visualise progress
		print("frame number", frameCount)

print("finish")

out.close()
video.release()
