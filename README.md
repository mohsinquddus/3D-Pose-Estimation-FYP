# Guide-Pose
In this era of efficiency and performance machines and systems tends to be better and faster.
Everything is being automate and self-aware for making lives easy and better than before. One
day we are working on computer vision and found a great idea of using computer vision latest
technique pose estimation in a way that we can produce a product that can change the future of
body fitness. It’s was a very vast about the pose estimation of human body. Pose estimation is a
computer vision technique that predicts and tracks the location of a person in an image or video.
We can also think of pose estimation as the problem of determining the position and orientation
of a camera relative to a given person and we done it by identifying, locating, and tracking a
number of Key Point’s on a given person. This project is designed to tackle with the wrong angle
exercise problem. Doing exercise in the wrong way not benefit the body at all, but it may cause
a lot of injuries. And it may cause the player to permanent loss to its physical body part. 



https://user-images.githubusercontent.com/42820866/132999687-dba77626-137d-468f-b0e0-25a8cf9f48a1.mp4


An automated pose estimator system will be helpful for the workout users that they do not have to
hire trainer. The application in their mobile helps the user to exercise anytime anywhere. The
points that return from the model are used get angle of different joints and then the angles are
used to predict the correct angles for specific exercises. To obtain the human body points we
experiment different models like openpose, Fastpose, alphapose, alphapose by GluonCV and at
last Mediapipe by google.

![frame1](https://user-images.githubusercontent.com/42820866/132999497-ae65335c-dedc-46a4-ae5d-0956176f8a0e.jpg)

After experimenting all these models, we are using Mediapipe. After
using the model, we use hardcoded angles to combine from the angles get out after the points
from the model, if the angle is correct we are communicating the user from the green or pink
color that the angle is correct and if the angle is wrong red color is used for the wrong line of the
skeleton. From this way the system communicates with the user and tells the right and wrong
angles and user do workout without any hesitation of muscle issue due to wrong angles exercise.



