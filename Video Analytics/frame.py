#EXTRACTING IMAGE by Video
import cv2
import os
import numpy as np
from glob import glob

vid = cv2.VideoCapture('E:/Video Analytics/Beauty of Nature.mp4')
currentframe = 0

#if my data folder doesnt exists in my current path,then make a new directory names DATA
if not os.path.exists('data'):
  os.makedirs('data')

#running a loop because I want to read my video object
#creating 2 variables
#sucess-is a boolean
#frame-contain my frame inforamtion of my video
#.read()-will extract frame by frame/ image by image information
while (True):
  success,frame = vid.read()
#video object,so can stop the video whenever I want to
  cv2.imshow(frame)
#store frame by frame infor by (.imwrite)method and
  #inside it i am passing my name of my image which i am going to save
  #'./data/frame-(.) will specofy the whole path before my data folder
  #str(currentframe)-this will make,each of my image will be name as frame1 and then next frame will be incremented starting from 0,
  #.jpg-want to store it in JPG
  #+frame- the frame i want to store
  cv2.imwrite('./data/frame' +str(currentframe)+'.jpg',frame)
  currentframe+=1
#can close the video object manually by typing "q" or until the video finshes
  if cv2.waitKey(1) & 0xFF == ord('q'):
    break
webCam.release()
cv2.destroyAllWindows()

