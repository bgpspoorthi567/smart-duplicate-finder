import cv2
import numpy as np

def extract_video_signature(path):
    try:
        cap = cv2.VideoCapture(path)
        frames = []

        for _ in range(5):
            ret, frame = cap.read()
            if not ret:
                break
            frame = cv2.resize(frame, (64, 64))
            frames.append(frame)

        cap.release()

        if not frames:
            return None

        return np.mean(frames, axis=0).flatten()
    except:
        return None
