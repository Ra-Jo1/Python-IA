# Two-Hand Detection with MediaPipe and OpenCV (Python)

## 📌 Description

This project uses **Python**, **OpenCV**, and **MediaPipe** to perform **real‑time detection of up to two hands** using a webcam.

The program:

*   Uses **MediaPipe Hand Landmarker** (task‑based API)
*   Detects and tracks **hand landmarks**
*   Converts normalized landmark coordinates into **pixel coordinates**
*   Draws landmarks on the video stream
*   Is structured using **functions** for clarity and reusability

***

## 🧰 Environment & Versions

*   **Python:** 3.14.3
*   **OpenCV:** 4.13.0
*   **MediaPipe:** 0.10.33

***

## 🧰 Requirements

*   Computer with a webcam
*   **Python 3.x**
*   Required Python libraries:
    *   `opencv-python`
    *   `mediapipe`
*   MediaPipe model file:
    *   `hand_landmarker.task`

***

## 📦 Installation

### Install dependencies

```bash
pip install opencv-python mediapipe
```

### Model File

Download the MediaPipe hand landmarker model and place it in your project folder:

    hand_landmarker.task

***

## ⚙️ How It Works

1.  Opens the webcam using **DirectShow (CAP\_DSHOW)** for better performance on Windows
2.  Sets camera parameters:
    *   Resolution: **1280 × 720**
    *   FPS: **30**
    *   Codec: **MJPG**
3.  Initializes a **MediaPipe Hand Landmarker** with:
    *   Detection mode: `VIDEO`
    *   Maximum hands: **2**
    *   Configurable confidence thresholds
4.  Each frame is:
    *   Converted from **BGR to RGB**
    *   Passed to MediaPipe with a timestamp
5.  Detected landmarks are:
    *   Converted from normalized coordinates to **pixel positions**
    *   Returned as structured lists via a function
6.  Landmarks are rendered as circles on the video stream
7.  Program exits when **`q`** is pressed

***

## ▶️ How to Use

1.  Connect a webcam to your computer
2.  Ensure `hand_landmarker.task` is in the correct directory
3.  Open the Python script
4.  Run the script:
    ```bash
    python hand_detection.py
    ```
5.  A window named **"my WEBcam"** will open
6.  Detected hand landmarks will appear in real time
7.  Press **`q`** to quit the program

***

## 🧩 Function Overview

### `parseLandmarkData(frame, landmarker)`

*   Detects hands in a frame
*   Converts normalized landmarks to pixel coordinates
*   Returns a list:
        [
          [(x1, y1), (x2, y2), ...],   # Hand 1
          [(x1, y1), (x2, y2), ...]    # Hand 2
        ]

This design makes it easy to reuse the function in other projects.

***

## 🧪 Adjustable Parameters

You can customize:

*   Camera resolution (`width`, `height`)
*   Number of detected hands (`num_hands`)
*   Confidence thresholds:
    *   Detection
    *   Presence
    *   Tracking

***

## 📝 Notes

*   MediaPipe Hand Landmarker provides **high‑precision hand tracking**
*   Detection works best with good lighting
*   FPS depends on resolution and system performance
*   This project is a strong base for:
    *   Gesture recognition
    *   Finger counting
    *   Sign language projects
    *   Human‑computer interaction (HCI)

***

## 📄 Author

**Ra‑Jo**

