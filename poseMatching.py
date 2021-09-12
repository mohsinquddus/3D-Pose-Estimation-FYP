import cv2 as cv
import numpy as np
import math
import pandas as pd
import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose



def weight_distance(pose1, pose2, conf1):

    sum1 = 1 / np.sum(conf1)

    sum2 = 0
    for i in range(len(pose1)):
        conf_ind = math.floor(i / 2) # each index i has x and y that share same confidence score
        sum2 += conf1[conf_ind] * abs(pose1[i] - pose2[i])

    weighted_dist = sum1 * sum2

    return weighted_dist


def similarity_score(pose1, pose2,conf1):
    p1 = []
    p2 = []
    pose_1 = np.array(pose1, dtype=np.float)
    pose_2 = np.array(pose2, dtype=np.float)

    # Normalize coordinates
    pose_1[:,0] = pose_1[:,0] / max(pose_1[:,0])
    pose_1[:,1] = pose_1[:,1] / max(pose_1[:,1])
    pose_2[:,0] = pose_2[:,0] / max(pose_2[:,0])
    pose_2[:,1] = pose_2[:,1] / max(pose_2[:,1])



    # Turn (16x2) into (32x1)
    for joint in range(pose_1.shape[0]):
        x1 = pose_1[joint][0]
        y1 = pose_1[joint][1]
        x2 = pose_2[joint][0]
        y2 = pose_2[joint][1]

        p1.append(x1)
        p1.append(y1)
        p2.append(x2)
        p2.append(y2)

    p1 = np.array(p1)
    p2 = np.array(p2)


    scoreB = weight_distance(p1, p2, conf1)

    return scoreB


# In[3]:


def get_pose_conf(results):
    pose = []
    conf = []
    for coor in results.pose_landmarks.landmark:
        x = coor.x
        y = coor.y
        visibility = coor.visibility
        pose.append((x,y))
        conf.append(visibility)
        
    return pose, conf


# In[4]:


def process_pose(pose1,pose2):
    pose1_new = np.array(pose1)
    pose2_new = np.array(pose2)

    pose1_new[:,0] = pose1_new[:,0] - min(pose1_new[:,0])
    pose1_new[:,1] = pose1_new[:,1] - min(pose1_new[:,1])

    pose2_new[:,0] = pose2_new[:,0] - min(pose2_new[:,0])
    pose2_new[:,1] = pose2_new[:,1] - min(pose2_new[:,1])

    resize_x = max(pose2_new[:,0])/max(pose1_new[:,0])
    resize_y = max(pose2_new[:,1])/max(pose1_new[:,1])

    pose1_new[:,0] = pose1_new[:,0] * resize_x
    pose1_new[:,1] = pose1_new[:,1] * resize_y
    
    
    return pose1_new, pose2_new




def poseMatching():
    cap = cv.VideoCapture(0)
    cap1 = cv.VideoCapture(2)
    
    with mp_pose.Pose(static_image_mode=True,min_detection_confidence=0.5) as pose:
        while cap.isOpened() :
            ret, frame1 = cap.read()
            ret1, frame2 = cap1.read()
            if ret==False or ret1 == False:
                break
                
            frame1 = cv.cvtColor(frame1, cv.COLOR_BGR2RGB)
            frame2 = cv.cvtColor(frame2, cv.COLOR_BGR2RGB)   
            text_new  = ""
            frame1.flags.writeable = False
            frame2.flags.writeable = False
            results1 = None
            results2 = None
            
            
            results2 = pose.process(frame2)
    
            results1 = pose.process(frame1)
            if results1.pose_landmarks == None or results2.pose_landmarks == None:
                text_new = "Unable to detect pose"
                color = (0,255,255)
    
            else:
                pose1,conf1 = get_pose_conf(results1)
                pose2,conf2 = get_pose_conf(results2)
    
                pose1_new, pose2_new = process_pose(pose1,pose2)
    
                score = similarity_score (pose1_new, pose2_new,conf1)
                if score<0.10:
                    text_new = "correct"
                    color = (255,255,0)
                else:
                    text_new = "not correct"
                    color = (255,0,255)
    
            frame1 = cv.cvtColor(frame1, cv.COLOR_RGB2BGR)
            frame2 = cv.cvtColor(frame2, cv.COLOR_RGB2BGR)
            frame1.flags.writeable = True
            frame2.flags.writeable = True
            cv.putText(frame1,text_new, (50, 50), cv.FONT_HERSHEY_SIMPLEX, 1, color, 2, cv.LINE_4)
            mp_drawing.draw_landmarks(
                frame1, results1.pose_landmarks, mp_pose.POSE_CONNECTIONS)
            mp_drawing.draw_landmarks(
                frame2, results2.pose_landmarks, mp_pose.POSE_CONNECTIONS)
            cv.imshow("frame2",frame1)
            cv.imshow("frame1",frame2)
            if cv.waitKey(1) & 0xFF == ord('q'):
                break
    
        cap.release()
        cv.destroyAllWindows()

