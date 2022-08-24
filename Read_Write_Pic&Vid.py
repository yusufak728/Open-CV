import cv2 as cv

# Reading Images

# img = cv.imread('opencv-course-master\Resources\Photos\cat_large.jpg')    #returns the image as pixels

# cv.imshow('Cat',img) # to display the img, 2 parameters name & the varible stored in

# cat_large goes off screen as the dimensions of the pic > dimensions of laptop, resizing reqd

#Reading Videos

capture = cv.VideoCapture('opencv-course-master\Resources\Videos\dog.mp4')        # takes integers or path, 0 -> webcam etc...
#use a while loop to view video frame by frame

while True:
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)
    
    if cv.waitKey(20) & 0xFF==ord('d'):  # to break out of the while loop, 'd' means when d key is pressed, break out of the loop
        break

capture.release()
cv.destroyAllWindows

# assertian,-215 failed error -> opencv couldn't find the file, in case of a video, the frames ran out
#cv.waitKey(0)