import cv2

def detect_cameras(max_cameras=10):
    cameras = []
    for i in range(max_cameras):
        cap = cv2.VideoCapture(i, cv2.CAP_DSHOW)
        if cap is None or not cap.isOpened():
            print(f'Camera not found: {i}')
        else:
            print(f'Camera found: {i}')
            cameras.append(i)
        cap.release()
    return cameras
