import cv2
import time
import os
import HandTrackingModule as htm


wCam, hCam= 640, 480


cap= cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)

folderPath= "Images"
mylist= os.listdir(folderPath)
#print(mylist)
overlayList= []

for imgPath in mylist:
    image= cv2.imread(f'{folderPath}/{imgPath}')
    #print(f'{folderPath}/{imgPath}')
    overlayList.append(image)

print(len(overlayList))
pTime=0

detector=htm.handDetector()
tipIds= [4,8,12,16,20]

while True:
    success, img= cap.read()
    img= detector.findHands(img)
    lmlist= detector.findPosition(img, draw=False)
    #print(lmlist)
    fingers=[]
    if len(lmlist)>=9:
        #thumb
        if lmlist[tipIds[0]][1]>lmlist[tipIds[0]-1][1]:
            fingers.append(1)
        else:
            fingers.append(0)

        for id in range(1,5):
            if lmlist[tipIds[id]][2]<lmlist[tipIds[id]-2][2]:
                fingers.append(1)
            else:
                fingers.append(0)
    #print(fingers)
    totalfingers=fingers.count(1)
    print(totalfingers)


    myimg=overlayList[totalfingers]
    a, b,c = myimg.shape
    #img[0:a,0:b]= myimg

    cTime= time.time()
    fps=1/(cTime-pTime)
    pTime=cTime

    cv2.putText(img, f'FPS:{int(fps)}',(400,70),cv2.FONT_HERSHEY_PLAIN,3,(255,0,0),3)

    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break