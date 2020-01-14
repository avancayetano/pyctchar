import cv2

def draw_ascii(img):
	frame = []
	chars = [" ", " ", ".", "+", "|", "%", "#", "@"]
	for row in img:
		frame.append([])
		for i in row:
			frame[-1].append(chars[i // 32])
	for row in frame:
		print("".join(row))

def capture():
	cap = cv2.VideoCapture(0)
	size = (200, 55)
	while(True):
		ret, frame = cap.read()
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		pixelated = cv2.resize(gray, size, interpolation=cv2.INTER_LINEAR)
		pixelated = cv2.flip(pixelated, 1)
		draw_ascii(pixelated)
	cap.release()

capture()
cv2.destroyAllWindows()
