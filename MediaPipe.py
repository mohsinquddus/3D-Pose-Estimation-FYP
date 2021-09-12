import cv2
import mediapipe as mp
import numpy as np
mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

def calculate_angle(a,b,c):
    a = np.array(a) # First
    b = np.array(b) # Mid
    c = np.array(c) # End

    radians = np.arctan2(c[1]-b[1], c[0]-b[0]) - np.arctan2(a[1]-b[1], a[0]-b[0])
    angle = np.abs(radians*180.0/np.pi)

    if angle >180.0:
        angle = 360-angle

    return angle

lvar=0
rvar=0

def create(arg=3):
    cap = cv2.VideoCapture(0)
    if (cap.isOpened() == False):
        print("Error reading video file")

    # We need to set resolutions.
    # so, convert them from float to integer.
    frame_width = int(cap.get(3))
    frame_height = int(cap.get(4))

    size = (frame_width, frame_height)

    # Below VideoWriter object will create
    # a frame of above defined The output
    # is stored in 'filename.avi' file.
    result = cv2.VideoWriter('filename.mp4',cv2.VideoWriter_fourcc(*'MP4V'),
                             30, size)## Setup mediapipe instance
    with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
        while cap.isOpened():
            ret, frame = cap.read()
            #frame = cv2.flip(frame, 1)
            width = int(cap.get(3))
            height = int(cap.get(4))
            # Recolor image to RGB
            try:
              image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            except:
              break
            image.flags.writeable = False

            # Make detection
            results = pose.process(image)
            if results.pose_landmarks == None:
                image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
                cv2.imshow("Live Angle Detection: Press 'q' to Exit",image)
                if cv2.waitKey(10) & 0xFF == ord('q'):
                    break
                continue
            # Recolor back to BGR
            image.flags.writeable = True
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
	    
            # Extract landmarks
            try:
                landmarks = results.pose_landmarks.landmark

                # Get coordinates
                #Shoulder
                Lshoulder = [landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x,landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y]
                Rshoulder = [landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].x,landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].y]
                #Elbow
                Lelbow = [landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].x,landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].y]
                Relbow = [landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].x,landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].y]
                #wRIST
                Lwrist = [landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].x,landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].y]
                Rwrist = [landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].x,landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].y]
                #Hip
                Lhip = [landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].x,landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].y]
                Rhip = [landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].x,landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].y]
                #Knee
                Lknee = [landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].x,landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].y]
                Rknee = [landmarks[mp_pose.PoseLandmark.RIGHT_KNEE.value].x,landmarks[mp_pose.PoseLandmark.RIGHT_KNEE.value].y]
                #Ankle
                Lankle = [landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value].x,landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value].y]
                Rankle = [landmarks[mp_pose.PoseLandmark.RIGHT_ANKLE.value].x,landmarks[mp_pose.PoseLandmark.RIGHT_ANKLE.value].y]

                #print(Lelbow,Lwrist,Lhip,Lknee,lankle)
                # Calculate angle

                #Elbow Angles
                Lelbowangle = calculate_angle(Lshoulder, Lelbow, Lwrist)
                #cv2.putText(image, str(int(Lelbowangle)), tuple(np.multiply(Lelbow, [1280, 720]).astype(int)),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
                cv2.putText(image, str(int(Lelbowangle)), tuple(np.multiply(Lelbow, [width, height]).astype(int)),cv2.FONT_HERSHEY_SIMPLEX, 0.25, (255, 0, 0), 1, cv2.LINE_AA)
                Relbowangle = calculate_angle(Rshoulder, Relbow, Rwrist)
                cv2.putText(image, str(int(Relbowangle)), tuple(np.multiply(Relbow, [width, height]).astype(int)),cv2.FONT_HERSHEY_SIMPLEX, 0.25, (255, 0, 0), 1, cv2.LINE_AA)

                #Shulders Angles
                Lshoulderangle = calculate_angle( Lelbow, Lshoulder, Lhip)
                cv2.putText(image, str(int(Lshoulderangle)), tuple(np.multiply(Lshoulder, [width, height]).astype(int)),cv2.FONT_HERSHEY_SIMPLEX, 0.25, (255, 0, 0), 1, cv2.LINE_AA)
                Rshoulderangle = calculate_angle( Relbow, Rshoulder, Rhip)
                cv2.putText(image, str(int(Rshoulderangle)), tuple(np.multiply(Rshoulder, [width, height]).astype(int)),cv2.FONT_HERSHEY_SIMPLEX, 0.25, (255, 0, 0), 1, cv2.LINE_AA)


                #Hip Angles
                Lhipangle = calculate_angle(Lshoulder, Lhip, Lknee)
                cv2.putText(image, str(int(Lhipangle)), tuple(np.multiply(Lhip, [width, height]).astype(int)),cv2.FONT_HERSHEY_SIMPLEX, 0.25, (255, 0, 0), 1, cv2.LINE_AA)
                Rhipangle = calculate_angle(Rshoulder, Rhip, Rknee)
                cv2.putText(image, str(int(Rhipangle)), tuple(np.multiply(Rhip, [width, height]).astype(int)),cv2.FONT_HERSHEY_SIMPLEX, 0.25, (255, 0, 0), 1, cv2.LINE_AA)

                #Knee Angles
                Lkneeangle = calculate_angle(Lhip, Lknee, Lankle)
                print(Lkneeangle)
                cv2.putText(image, str(int(Lkneeangle)), tuple(np.multiply(Lknee, [width, height]).astype(int)),cv2.FONT_HERSHEY_SIMPLEX, 0.25, (255, 0, 0), 1, cv2.LINE_AA)
                Rkneeangle = calculate_angle(Rhip, Rknee, Rankle)
                cv2.putText(image, str(int(Rkneeangle)), tuple(np.multiply(Rknee, [width, height]).astype(int)),cv2.FONT_HERSHEY_SIMPLEX, 0.25, (255, 0, 0), 1, cv2.LINE_AA)

                #Visualizing Angles
                print("Shoulder",Lshoulderangle , Rshoulderangle)
                print("Elbow", Lelbowangle, Relbowangle)
                #print("Hip", Lhipangle, Rhipangle)
                #print("Knee", Lkneeangle, Rkneeangle)

            except:
                print("In Except")
                pass

            #print(mp_pose.POSE_CONNECTIONS)
            # Render detections
            mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                                    mp_drawing.DrawingSpec(color=(245,117,66), thickness=2, circle_radius=2),
                                    mp_drawing.DrawingSpec(color=(245,66,230), thickness=2, circle_radius=2) )
            def squat():
              #Knee Angles
              if Lkneeangle > 180 or Lkneeangle <75:
                cv2.line(image, tuple(np.multiply(Lhip, [width, height]).astype(int)) , tuple(np.multiply(Lknee, [width, height]).astype(int)), (0,0,255), 2)
                cv2.line(image, tuple(np.multiply(Lknee, [width, height]).astype(int)) , tuple(np.multiply(Lankle, [width, height]).astype(int)), (0,0,255), 2)
              if Rkneeangle > 180 or Rkneeangle <50:
                cv2.line(image, tuple(np.multiply(Rhip, [width, height]).astype(int)) , tuple(np.multiply(Rknee, [width, height]).astype(int)), (0,0,255), 2)
                cv2.line(image, tuple(np.multiply(Rknee, [width, height]).astype(int)) , tuple(np.multiply(Rankle, [width, height]).astype(int)), (0,0,255), 2)
              #Hip Angles
              if Lhipangle > 180 or Lhipangle < 73:
                cv2.line(image, tuple(np.multiply(Lshoulder, [width, height]).astype(int)) , tuple(np.multiply(Lhip, [width, height]).astype(int)), (0,0,255), 2)
                cv2.line(image, tuple(np.multiply(Lhip, [width, height]).astype(int)) , tuple(np.multiply(Lknee, [width, height]).astype(int)), (0,0,255), 2)
              if Lhipangle > 180 or Lhipangle < 73:
                cv2.line(image, tuple(np.multiply(Rshoulder, [width, height]).astype(int)) , tuple(np.multiply(Rhip, [width, height]).astype(int)), (0,0,255), 2)
                cv2.line(image, tuple(np.multiply(Rhip, [width, height]).astype(int)) , tuple(np.multiply(Rknee, [width, height]).astype(int)), (0,0,255), 2)

            #squat()

            def shoulder():
              #Shoulders Angles
              if Lshoulderangle < 65 or Lshoulderangle >170:
                cv2.line(image, tuple(np.multiply(Lhip, [width, height]).astype(int)) , tuple(np.multiply(Lshoulder, [width, height]).astype(int)), (0,0,255), 2)
                cv2.line(image, tuple(np.multiply(Lshoulder, [width, height]).astype(int)) , tuple(np.multiply(Lelbow, [width, height]).astype(int)), (0,0,255), 2)
              if Rshoulderangle < 65 or Rshoulderangle >170:
                cv2.line(image, tuple(np.multiply(Rhip, [width, height]).astype(int)) , tuple(np.multiply(Rshoulder, [width, height]).astype(int)), (0,0,255), 2)
                cv2.line(image, tuple(np.multiply(Rshoulder, [width, height]).astype(int)) , tuple(np.multiply(Relbow, [width, height]).astype(int)), (0,0,255), 2)
              #Elbow Angles
              if Lelbowangle < 48 or Lelbowangle > 174:
                cv2.line(image, tuple(np.multiply(Lshoulder, [width, height]).astype(int)) , tuple(np.multiply(Lelbow, [width, height]).astype(int)), (0,0,255), 2)
                cv2.line(image, tuple(np.multiply(Lelbow, [width, height]).astype(int)) , tuple(np.multiply(Lwrist, [width, height]).astype(int)), (0,0,255), 2)
              if Relbowangle < 48 or Relbowangle > 174:
                cv2.line(image, tuple(np.multiply(Rshoulder, [width, height]).astype(int)) , tuple(np.multiply(Relbow, [width, height]).astype(int)), (0,0,255), 2)
                cv2.line(image, tuple(np.multiply(Relbow, [width, height]).astype(int)) , tuple(np.multiply(Rwrist, [width, height]).astype(int)), (0,0,255), 2)
            def bicep():
              #Shoulders Angles
              if Lshoulderangle > 10: 
                cv2.line(image, tuple(np.multiply(Lhip, [width, height]).astype(int)) , tuple(np.multiply(Lshoulder, [width, height]).astype(int)), (0,0,255), 2)
                cv2.line(image, tuple(np.multiply(Lshoulder, [width, height]).astype(int)) , tuple(np.multiply(Lelbow, [width, height]).astype(int)), (0,0,255), 2)
              if Rshoulderangle > 10:
                cv2.line(image, tuple(np.multiply(Rhip, [width, height]).astype(int)) , tuple(np.multiply(Rshoulder, [width, height]).astype(int)), (0,0,255), 2)
                cv2.line(image, tuple(np.multiply(Rshoulder, [width, height]).astype(int)) , tuple(np.multiply(Relbow, [width, height]).astype(int)), (0,0,255), 2)
              #Elbow Angles
              try:
                print("previous New",pLelbowangle,pRelbowangle)
                if pLelbowangle-Lelbowangle < 0 and Lelbowangle < 40:
                  cv2.line(image, tuple(np.multiply(Lshoulder, [width, height]).astype(int)) , tuple(np.multiply(Lelbow, [width, height]).astype(int)), (0,0,255), 2)
                  cv2.line(image, tuple(np.multiply(Lelbow, [width, height]).astype(int)) , tuple(np.multiply(Lwrist, [width, height]).astype(int)), (0,0,255), 2)
                if pRelbowangle-Relbowangle < 0:
                  cv2.line(image, tuple(np.multiply(Rshoulder, [width, height]).astype(int)) , tuple(np.multiply(Relbow, [width, height]).astype(int)), (0,0,255), 2)
                  cv2.line(image, tuple(np.multiply(Relbow, [width, height]).astype(int)) , tuple(np.multiply(Rwrist, [width, height]).astype(int)), (0,0,255), 2)
              except:
                pass

            print("Next",Lelbowangle,Relbowangle)
            pLelbowangle = Lelbowangle
            pRelbowangle = Relbowangle

            if arg ==1:
                squat()
                print("SQUAT")
            elif arg==2:
                shoulder()
                print("SHOULDER")
            elif arg==3:
                bicep()
                print("BICEP")

            print("Image Size", image.shape)
            cv2.imshow("Live Angle Detection: Press 'q' to Exit",image)
            result.write(image)
            print("Successfully Saved Frame")
            if cv2.waitKey(10) & 0xFF == ord('q'):
                break



        cap.release()
        #video.release()
        result.release()
        cv2.destroyAllWindows()
    #print("Success")
