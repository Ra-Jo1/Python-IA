#This program use function to detect 2 hands, version of python 3.14.3, cv2 4.13.0 and mediapipe 0.10.33

import time  # used to generate timestamps for video frames
import cv2  # OpenCV for camera capture and display
import mediapipe as mp

from mediapipe.tasks.python.core import base_options  # MediaPipe task base option handling
from mediapipe.tasks.python.vision.core import vision_task_running_mode  # Running mode enum for MediaPipe vision tasks
from mediapipe.tasks.python.vision import hand_landmarker  # Hand landmarker task API
from mediapipe.tasks.python.vision.core import image as mp_image  # Image wrapper used by MediaPipe tasks

print(cv2.__version__)  # print OpenCV version for debugging
print(mp.__version__)

MODEL_PATH = "hand_landmarker.task"  # Path to the MediaPipe hand landmarker model file
width = 1280  # desired capture width
height = 720  # desired capture height

options = hand_landmarker.HandLandmarkerOptions(
    base_options=base_options.BaseOptions(model_asset_path=MODEL_PATH),  # set the model path
    running_mode=vision_task_running_mode.VisionTaskRunningMode.VIDEO,  # use video mode for sequential frames
    num_hands=2,  # maximum number of hands to detect
    min_hand_detection_confidence=0.5,  # required detection confidence threshold
    min_hand_presence_confidence=0.5,  # required hand presence confidence threshold
    min_tracking_confidence=0.5,  # required tracking confidence threshold
)

def parseLandmarkData(frame, landmarker):
    """Return list of hands where each hand is a list of (x, y) pixel tuples."""

    myHands = []  # list to store landmarks for all detected hands

    # Convert from BGR (OpenCV) to RGB (MediaPipe expects RGB)
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Wrap the numpy frame into MediaPipe Image object
    mp_image_obj = mp_image.Image(mp_image.ImageFormat.SRGB, frame_rgb)

    # Use current time as timestamp (ms) for the video frame
    timestamp_ms = int(time.time() * 1000)

    # Run hand landmark detection on the frame
    results = landmarker.detect_for_video(mp_image_obj, timestamp_ms)

    # If any hand landmarks are found, convert normalized landmark coords to pixel coords
    if results.hand_landmarks:
        for hand_landmarks in results.hand_landmarks:
            myHand = []
            for landmark in hand_landmarks:
                # landmark.x and landmark.y are normalized [0..1] coordinates
                myHand.append((int(landmark.x * width), int(landmark.y * height)))
            myHands.append(myHand)

    return myHands


# Initialize camera capture
cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)  # use DirectShow backend on Windows
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)  # set capture width
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)  # set capture height
cam.set(cv2.CAP_PROP_FPS, 30)  # set target framerate
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*"MJPG"))  # set camera format for better performance

# Create the MediaPipe hand landmarker and run it in a context manager so it closes cleanly
with hand_landmarker.HandLandmarker.create_from_options(options) as hands:
    while True:
        # Grab a frame from the camera
        has_frame, frame = cam.read()
        if not has_frame:
            break  # stop if camera frame is not available

        frame = cv2.resize(frame, (width, height))  # normalize frame size
        landmarks = parseLandmarkData(frame, hands)  # detect hand landmarks

        # Optional: draw detected landmarks on the frame
        for hand in landmarks:
            for (x, y) in hand:
                cv2.circle(frame, (x, y), 2, (255, 255, 0), 3)

        # Show frame
        cv2.imshow("my WEBcam", frame)
        cv2.moveWindow("my WEBcam", 0, 0)  # place window at top-left

        # Exit when the user presses 'q'
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

cam.release()  # release camera resources
cv2.destroyAllWindows()  # close OpenCV windows
