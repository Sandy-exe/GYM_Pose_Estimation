import cv2
import mediapipe as mp
import numpy as np
import threading
import time
from modules.pose_estimation import PoseEstimator
from modules.angle_calculation import calculate_angle
from modules.text_to_speech import speak
from modules.camera_detection import detect_cameras

def main():
    cap = cv2.VideoCapture(0)
    
    if not cap.isOpened():
        print("Error: Camera not found.")
        return

    pose_estimator = PoseEstimator(min_detection_confidence=0.5, min_tracking_confidence=0.5)
    bd = False
    start_time = time.time()
    mp_pose = mp.solutions.pose

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = pose_estimator.process(image)
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        try:
            if results and results.pose_landmarks:
                landmarks = results.pose_landmarks.landmark

                # Calculate angles
                left_shoulder = [landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x,
                                 landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y]
                left_elbow = [landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].x,
                              landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].y]
                left_wrist = [landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].x,
                              landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].y]
                left_elbow_angle = calculate_angle(left_shoulder, left_elbow, left_wrist)

                right_shoulder = [landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].x,
                                  landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].y]
                right_elbow = [landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].x,
                               landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].y]
                right_wrist = [landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].x,
                               landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].y]
                right_elbow_angle = calculate_angle(right_shoulder, right_elbow, right_wrist)

                cv2.putText(image, f"Right Elbow Angle: {right_elbow_angle:.2f}", 
                            tuple(np.multiply(right_elbow, [640, 480]).astype(int)), 
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)

                if right_elbow_angle > 110:
                    cv2.putText(image, "Bad posture in Right ARM", (10, 50),
                                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)

                if right_elbow_angle > 110 and not bd:
                    threading.Thread(target=speak, args=("Bad Posture Detected",)).start()
                    bd = True
                    start_time = time.time()

                if right_elbow_angle < 110 and bd:
                    bd = False

        except Exception as e:
            print(f"Error processing frame: {e}")

        pose_estimator.draw_landmarks(image)
        cv2.imshow('Mediapipe Feed', image)

        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
