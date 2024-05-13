from time import strftime
import cv2
import os
from keras.models import load_model
import numpy as np
import time

import imagehash
from PIL import Image
import cv2
import sys
import os
import imutils
from scipy.spatial import distance as dist
from imutils import face_utils
import argparse
import time
import dlib
import math
import cv2
import numpy as np
from EAR import eye_aspect_ratio
from MAR import mouth_aspect_ratio
from HeadPose import getHeadTiltAndCoords
import pyttsx3
from datetime import datetime
engine = pyttsx3.init()
name="attentive"
if os.path.exists(name):
    h=0
else:
    os.mkdir(name)
now = datetime.now()
dt_string = now.strftime("%Y_%m_%d")


student_list=[]

def SpeakText(command):
    engine = pyttsx3.init()
    print(command)
    engine.say(command)
    engine.runAndWait()
    engine.stop()
print("[INFO] loading facial landmark predictor...")
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')


print("[INFO] initializing camera...")
vs =  cv2.VideoCapture(0)
time.sleep(2.0)
frame_width = 1024
frame_height = 576


image_points = np.array([
    (359, 391),     # Nose tip 34
    (399, 561),     # Chin 9
    (337, 297),     # Left eye left corner 37
    (513, 301),     # Right eye right corne 46
    (345, 465),     # Left Mouth corner 49
    (453, 469)      # Right mouth corner 55
], dtype="double")

(lStart, lEnd) = face_utils.FACIAL_LANDMARKS_IDXS["left_eye"]
(rStart, rEnd) = face_utils.FACIAL_LANDMARKS_IDXS["right_eye"]

EYE_AR_THRESH = 0.25
MOUTH_AR_THRESH = 0.70
EYE_AR_CONSEC_FRAMES = 3
COUNTER = 0

(mStart, mEnd) = (49, 68)
def SpeakText(command):

    print(command)
    engine.say(command)
    engine.runAndWait()
    engine.stop()
def image_matching(a,b):
    i1 = Image.open(a)
    i2 = Image.open(b)
    assert i1.mode == i2.mode, "Different kinds of images."
    assert i1.size == i2.size, "Different sizes."
    pairs = zip(i1.getdata(), i2.getdata())
    if len(i1.getbands()) == 1:
    # for gray-scale jpegs
        dif = sum(abs(p1-p2) for p1,p2 in pairs)
    else:
        dif = sum(abs(c1-c2) for p1,p2 in pairs for c1,c2 in zip(p1,p2))
    ncomponents = i1.size[0] * i1.size[1] * 3
    xx= (dif / 255.0 * 100) / ncomponents
    return xx
def match_templates(in_image):
    name=[]
    values=[]
    entries = os.listdir('train/')
    folder_lenght= len(entries)
    i=0
    for x in entries:
        val=100
        directory=x
        name.append(x)
        x1="train/"+x
        arr = os.listdir(x1)
        for x2 in arr:
             path=x1+"/"+str(x2)
             find=image_matching(path,in_image)
             hash0 = imagehash.average_hash(Image.open(path))
             hash1 = imagehash.average_hash(Image.open(in_image))
             cc1=hash0 - hash1
             find=cc1
             if(find<val):
                 val=find
        values.append(val)
    values_lenght= len(values)
    pos=0;
    pos_val=100
    for x in range(0, values_lenght):
        if values[x]<pos_val:
            pos=x
            pos_val=values[x]
    if(pos_val<16):
        print(pos,pos_val,name[pos])
        return name[pos]
    else:
        return "unknown"
face = cv2.CascadeClassifier('haar cascade files\haarcascade_frontalface_alt.xml')
leye = cv2.CascadeClassifier('haar cascade files\haarcascade_lefteye_2splits.xml')
reye = cv2.CascadeClassifier('haar cascade files\haarcascade_righteye_2splits.xml')
count=0
score=0
thicc=2
rpred=[99]
lpred=[99]
facepred=[99]
yawning=0
sleeping=0
model = load_model('models/cnnCat2.h5')
cascPath = "haar cascade files/haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascPath)
train=True
video_capture = cv2.VideoCapture(0)
name="testing"
if os.path.exists(name):
    h=0;
else:
    os.mkdir(name)
e_mail=0
while True:
    ret, frame = video_capture.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
######
    if (frame is None):
            print("Can't open image file")
    face_cascade = cv2.CascadeClassifier(cascPath)
    faces = face_cascade.detectMultiScale(frame, 1.1, 3, minSize=(100, 100))
    if (faces is None):
            print('Failed to detect face')
    if (True):
            for (x, y, w, h) in faces:
                dd=0
    facecnt = len(faces)
    i = 0

    height, width = frame.shape[:2]
    for (x, y, w, h) in faces:
            r = max(w, h) / 2
            centerx = x + w / 2
            centery = y + h / 2
            nx = int(centerx - r)
            ny = int(centery - r)
            nr = int(r * 2)
            faceimg = frame[ny:ny+nr, nx:nx+nr]
            font = cv2.FONT_HERSHEY_SIMPLEX
            str1=name+'\\tt.jpg'
            # kk=kk+1
            lastimg = cv2.resize(faceimg, (100, 100))
            cv2.imwrite(str1, lastimg)
            ar=match_templates(str1)
            if ar=="unknown":
                dd=0
            else:
                height,width = frame.shape[:2]
                faceimg = frame[ny:ny + nr, nx:nx + nr]
                # cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
                cv2.putText(faceimg, (ar), (10,70), cv2.FONT_HERSHEY_SIMPLEX, 1,(0,255,0),1,cv2.LINE_AA)
            ########################################
                frame = imutils.resize(frame, width=1024, height=576)
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                size = gray.shape
                rects = detector(gray, 0)

                if len(rects) > 0:
                    text = "{} face(s) found".format(len(rects))
                    cv2.putText(frame, text, (10, 20),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

                for rect in rects:
                    (bX, bY, bW, bH) = face_utils.rect_to_bb(rect)
                    cv2.rectangle(frame, (bX, bY), (bX + bW, bY + bH), (0, 255, 0), 1)
                    shape = predictor(gray, rect)
                    shape = face_utils.shape_to_np(shape)

                    leftEye = shape[lStart:lEnd]
                    rightEye = shape[rStart:rEnd]
                    leftEAR = eye_aspect_ratio(leftEye)
                    rightEAR = eye_aspect_ratio(rightEye)
                    ear = (leftEAR + rightEAR) / 2.0

                    leftEyeHull = cv2.convexHull(leftEye)
                    rightEyeHull = cv2.convexHull(rightEye)
                    cv2.drawContours(frame, [leftEyeHull], -1, (0, 255, 0), 1)
                    cv2.drawContours(frame, [rightEyeHull], -1, (0, 255, 0), 1)

                    if ear < EYE_AR_THRESH:
                        COUNTER += 1
                        if COUNTER >= EYE_AR_CONSEC_FRAMES:
                            cv2.putText(frame, "Eyes Closed!", (500, 20),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
                            sleeping+=1
                    else:
                        COUNTER = 0
                        sleeping=0

                    mouth = shape[mStart:mEnd]
                    mouthMAR = mouth_aspect_ratio(mouth)
                    mar = mouthMAR
                    mouthHull = cv2.convexHull(mouth)
                    cv2.drawContours(frame, [mouthHull], -1, (0, 255, 0), 1)
                    # cv2.putText(frame, "MAR: {:.2f}".format(mar), (650, 20),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

                    if mar > MOUTH_AR_THRESH:
                        # cv2.putText(frame, "Yawning!", (800, 20),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
                        yawning+=1
                    else:
                        yawning=0

                    # for (i, (x, y)) in enumerate(shape):
                    #     if i == 33:
                    #         image_points[0] = np.array([x, y], dtype='double')
                    #         cv2.circle(frame, (x, y), 1, (0, 255, 0), -1)
                    #         cv2.putText(frame, str(i + 1), (x - 10, y - 10),cv2.FONT_HERSHEY_SIMPLEX, 0.35, (0, 255, 0), 1)
                    #     elif i == 8:
                    #         image_points[1] = np.array([x, y], dtype='double')
                    #         cv2.circle(frame, (x, y), 1, (0, 255, 0), -1)
                    #         cv2.putText(frame, str(i + 1), (x - 10, y - 10),cv2.FONT_HERSHEY_SIMPLEX, 0.35, (0, 255, 0), 1)
                    #     elif i == 36:
                    #         image_points[2] = np.array([x, y], dtype='double')
                    #         cv2.circle(frame, (x, y), 1, (0, 255, 0), -1)
                    #         cv2.putText(frame, str(i + 1), (x - 10, y - 10),cv2.FONT_HERSHEY_SIMPLEX, 0.35, (0, 255, 0), 1)
                    #     elif i == 45:
                    #         image_points[3] = np.array([x, y], dtype='double')
                    #         cv2.circle(frame, (x, y), 1, (0, 255, 0), -1)
                    #         cv2.putText(frame, str(i + 1), (x - 10, y - 10),cv2.FONT_HERSHEY_SIMPLEX, 0.35, (0, 255, 0), 1)
                    #     elif i == 48:
                    #         image_points[4] = np.array([x, y], dtype='double')
                    #         cv2.circle(frame, (x, y), 1, (0, 255, 0), -1)
                    #         cv2.putText(frame, str(i + 1), (x - 10, y - 10),cv2.FONT_HERSHEY_SIMPLEX, 0.35, (0, 255, 0), 1)
                    #     elif i == 54:
                    #         image_points[5] = np.array([x, y], dtype='double')
                    #         cv2.circle(frame, (x, y), 1, (0, 255, 0), -1)
                    #         cv2.putText(frame, str(i + 1), (x - 10, y - 10),cv2.FONT_HERSHEY_SIMPLEX, 0.35, (0, 255, 0), 1)
                    #     else:
                    #         cv2.circle(frame, (x, y), 1, (0, 0, 255), -1)
                    #         cv2.putText(frame, str(i + 1), (x - 10, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.35, (0, 0, 255), 1)
                    # for p in image_points:
                    #     cv2.circle(frame, (int(p[0]), int(p[1])), 3, (0, 0, 255), -1)
                    if yawning >= 3:
                        SpeakText(ar+" is Yawning")
                        # ar+=":Yawning"
                        student_list.append(""+ar+" # "+"Yawning")

                    if sleeping>=3:
                        SpeakText(ar+" is Sleeping")
                        # ar += ":Sleeping"
                        student_list.append("" + ar + " # " + "Sleeping")




                    # (head_tilt_degree, start_point, end_point,end_point_alt) = getHeadTiltAndCoords(size, image_points, frame_height)
                    #
                    # if head_tilt_degree:
                    #     cv2.putText(frame, 'Head Tilt Degree: ' + str(head_tilt_degree[0]), (170, 20),
                    #                 cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

    frame = imutils.resize(frame, width=1024, height=576)
    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        print(student_list)
        result=""
        for x in student_list:
            result+=x+"\n"

        file=os.path.join("attentive" + "/" + dt_string + '.txt')
        print(file)
        with open((file), 'w') as f:
            f.writelines(result)
        f.close()

        break

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()

