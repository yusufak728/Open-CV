import cv2 as cv


def rescaleFrame(frame, scale = 0.75):
    # will work for images, videos and live videos
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)  #0-> width, 1-> height
    dimension = (width, height)

    return cv.resize(frame, dimension, interpolation=cv.INTER_AREA)

# Reading Images

img = cv.imread('opencv-course-master\Resources\Photos\cat.jpg')    #returns the image as pixels

cv.imshow('Cat',img)

resized_image = rescaleFrame(img)
cv.imshow('Image', resized_image)

#Reading Videos

capture = cv.VideoCapture('opencv-course-master\Resources\Videos\dog.mp4')        # takes integers or path, 0 -> webcam etc...
#use a while loop to view video frame by frame

while True:
    isTrue, frame = capture.read()
    frame_resized = rescaleFrame(frame, scale= 0.2)  # default -> 75% of original

    cv.imshow('Video', frame)
    cv.imshow('Video Resized', frame_resized)
    
    if cv.waitKey(20) & 0xFF==ord('d'):  # to break out of the while loop, 'd' means when d key is pressed, break out of the loop
        break

capture.release()
cv.destroyAllWindows


# def changeRes(width, height):
#     # Live Videos only (external camera or webcam)
#     capture.set(3, width)
#     capture.set(3, height)