# this script converts each frame of the original video into a 36x28 image
# then it creates an array containing each image where
# each image is an array of 1s and 0s, 1 being black and 0 being white
# the final result is in data.json

from PIL import Image
import os
import json
import cv2

IMAGES = 6572

# resize each frame into 36x28 images
for i in range(1, IMAGES+1):
    image = cv2.imread("./frames/"+str(i)+".png")
    image = cv2.resize(image, (36, 28), interpolation=cv2.INTER_CUBIC)
    cv2.imwrite("./resizedFrames/"+str(i)+".png", image)


frames = []
frame = []
row = []

# convert each pixel into 1 if it's black and 0 if it's white
for f in range(1, IMAGES+1):
    im = Image.open("./resizedFrames/"+str(f)+".png")
    image = im.load()
    x, y = im.size
    frame = []
    for a in range(y):
        row = []
        for b in range(x):
            if image[b,a][0]<200:
                row.append(1)
            else:
                row.append(0)
        frame.append(row)
    frames.append(frame)

file = open(os.path.realpath(os.path.join(os.path.dirname(__file__))) + "\\data.json", 'w')
file.write(json.dumps(frames))
file.close()