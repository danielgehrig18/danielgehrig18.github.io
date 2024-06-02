import cv2 

img = cv2.imread("header_one_orig.jpg")
a = 0.8
img = (a * 255 +  (1-a)*img.astype("float32")).astype("uint8")
cv2.imwrite("header_one.jpg", img)
