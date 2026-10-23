import cv2

video = cv2.VideoCapture('bad_apple.mp4')
out = open("bad_apple.txt", "a")

fontSize = 5

chars = [' ', '.', ':', '-', '=', '+', '*', '#', '%', '@', '@']
width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))

print("start")

while True:
	ret, frameOG = video.read()
	if not ret:
		break

	gray_img = cv2.cvtColor(frameOG, cv2.COLOR_BGR2GRAY)
	_, frame = cv2.threshold(gray_img, 127, 255, cv2.THRESH_BINARY)

	art = []

	#generates the ascii art
	for y in range(height//int(fontSize*1.5)): #navigates the y cordinant
		artLine = [] #one line of the result
		for x in range(width//int(fontSize*0.6)): #makes one line of the result
			whites = 0
			for a in range(int(fontSize*1.5)): #navigates the y cordinant
				for b in range(int(fontSize*0.6)): #navigates the x cordinant
					if frame[a+(int(fontSize*1.5)*y), b+(int(fontSize*0.6)*x)] == 255:
						whites += 1;

			artLine.append(chars[int((whites/(int(fontSize*1.5)*int(fontSize*0.6)))*10)])
		art.append(artLine)

	for c in art: #print the image
		for d in c:
			out.write(str(d))
		out.write('\n')
	out.write(";\n")

print("finish")

out.close()
video.release()