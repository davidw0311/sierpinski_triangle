import cv2 
import numpy as np
import random

from PIL import Image

    
XMAX = 1000
YMAX = 1000
BORDER = 100

corners = {1:(XMAX//2, 0), 2:(0,YMAX), 3:(XMAX,YMAX)}

def getMidPoint(x1,y1,x2,y2):
    return ((x1+x2)//2, (y1+y2)//2)

img = np.zeros((XMAX,YMAX))

x = XMAX//2
y = YMAX//2

limg = np.zeros((XMAX+2*BORDER, YMAX+2*BORDER))

frames = []
for i in range(10000):
    (cx,cy) = random.choice(list(corners.values()))
    (x,y) = getMidPoint(x,y,cx,cy)
    limg[BORDER+y, BORDER+x]=255 
    if i %10 == 0:
        frames.append(Image.fromarray(limg))
    if i % 1000 == 0:
        print('frame', i)
        
cv2.imwrite("sierpinski.jpg",limg)


frame_one = frames[0]
print("saving gif ...")
frame_one.save("sierpinski.gif", format="GIF", append_images=frames,
        save_all=True, loop=0)
    