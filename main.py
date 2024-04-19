import cv2
from PIL import Image

from util import get_limits


yellow = [0, 255, 255]  # yellow in BGR colorspace
cap = cv2.VideoCapture(0) # how many webcamp you have on your setup, (I have only one camera so my index will be 0)
while True:
    ret, frame = cap.read()  # while true code is  going to read the frame from the webcam

# From here color detection starts
    hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) # visualizing the frame in HSV colorspace

    lowerLimit, upperLimit = get_limits(color=yellow)

    mask = cv2.inRange(hsvImage, lowerLimit, upperLimit) # mask of the yellow color we want to detect, it's interval

    mask_ = Image.fromarray(mask) # converting the our image from numpy array to PIL image (for OpenCV compatibility)

    bbox = mask_.getbbox() # getting the bounding box of the detected color

    if bbox is not None:
        x1, y1, x2, y2 = bbox 

        frame = cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 5)

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()

cv2.destroyAllWindows()
