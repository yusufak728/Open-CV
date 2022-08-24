#pylint:disable=no-member

import cv2 as cv

# Read in an image
img = cv.imread('opencv-course-master\Resources\Photos\park.jpg')
# cv.imshow('Park', img)


# # Converting to grayscale
# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray', gray)

# # Blur 
blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)   #7,7 -> has to be an odd number, increasing will make it more blur
# cv.imshow('Blur', blur)

# # Edge Cascade
canny = cv.Canny(img, 125, 175)  # can keep blur instead of img, reduces edges
# cv.imshow('Canny Edges', canny)

# # Dilating the image
dilated = cv.dilate(canny, (7,7), iterations=3)
# cv.imshow('Dilated', dilated)

# # Eroding
eroded = cv.erode(dilated, (7,7), iterations=3)
# cv.imshow('Eroded', eroded)  #gives back image before dilation, to get the edges back , edge cascade

# # Resize
resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC) #inter area, linear
# cv.imshow('Resized', resized)

# # Cropping
cropped = img[50:200, 200:400]
cv.imshow('Cropped', cropped)

cv.waitKey(0)