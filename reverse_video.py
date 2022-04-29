import cv2
from cv2 import VideoCapture
import numpy as np

#array for saving frames
input_frames=[]

#reading video
vid = VideoCapture('clip.mp4')

#reading first frame
success,img = vid.read()


w=int(vid.get(3))
h=int(vid.get(4))
count = 0

size = (w,h)
while success:
  
  #if you want to save all the frames uncomment the below line
  #cv2.imwrite("frame%d.jpg" % count, img)
  if success == True:

    success,img = vid.read()
    input_frames.append(img)
    count += 1
  
  else:
    break

input_frames.pop()

#revering frames to reverse the video
input_frames.reverse()

out = cv2.VideoWriter('reverse_vid.avi',cv2.VideoWriter_fourcc(*'DIVX'), 25, size)

for i in input_frames:
  out.write(i)
  if cv2.waitKey(25) and 0xFF == ord("q"):
    break

out.release()
cv2.destroyAllWindows()
