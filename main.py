import cv2, sys, os

def draw_ascii(img, low, high):
	frame = []
	chars = [" ", " ", ".", "+", "|", "%", "#", "@"]
	for row in img:
		frame.append([])
		for i in row:
			frame[-1].append(chars[interpolate(i, low, high) // (256 // len(chars))])
	for row in frame:
		print("".join(row))

# find the interpolated value relative to the darkest and lightest pixel value
def interpolate(val, low, high):
	return int((val - low) / (high - low) * (255 - 0)) + 0 


# finds the darkest (low) and lightest (high) pixel value of the grayscaled image
def find_low_high(img):
	low = 255
	high = 0
	for row in img:
		for i in row:
			if i < low:
				low = i
			if i > high:
				high = i
	return low, high


def capture():
	cap = cv2.VideoCapture(0)
	width, height = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
	sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=height, cols=width)) # changes terminal dimensions
	size = (200, 55)
	while(True):
		ret, frame = cap.read()
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		pixelated = cv2.resize(gray, size, interpolation=cv2.INTER_LINEAR)
		pixelated = cv2.flip(pixelated, 1)
		low, high = find_low_high(pixelated)
		draw_ascii(pixelated, low, high)
	cap.release()

capture()
cv2.destroyAllWindows()
