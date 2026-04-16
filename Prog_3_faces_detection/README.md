# Multiple Face Detection with OpenCV (Python)

## 📌 Description

This project uses **Python 3** and **OpenCV** to perform **real‑time multiple face detection** using a webcam.

It captures video frames, converts them to grayscale for better performance, and detects faces using a **Haar Cascade classifier**, drawing a rectangle around each detected face.

***

## 🧰 Requirements

*   Computer with a webcam
*   **Python 3.x**
*   **OpenCV (cv2)** library
*   Haar Cascade XML file: 
    *   `haarcascade_frontalface_default.xml`

***

## 📦 Installation

### Install OpenCV

```bash
pip install opencv-python
```

### Haar Cascade File

Download the model from the official OpenCV repository and place it in:

    haar/haarcascade_frontalface_default.xml

***

## ⚙️ How It Works

1.  Opens the webcam using **DirectShow (CAP\_DSHOW)** for faster access (Windows)
2.  Sets camera parameters:
    *   Resolution: **640 × 360**
    *   FPS: **30**
    *   Codec: **MJPG**
3.  Captures frames continuously
4.  Converts each frame to **grayscale** to reduce computation
5.  Detects multiple faces using the Haar Cascade model
6.  Draws a **blue rectangle** around each detected face
7.  Displays the video stream in real time
8.  Stops when the **`q` key** is pressed

***

## ▶️ How to Use

1.  Connect a webcam to your computer
2.  Make sure the Haar Cascade file path is correct
3.  Open the Python script
4.  Run the script:
    ```bash
    python face_detection.py
    ```
5.  A window named **"Yo\_world"** will open showing detected faces
6.  Press **`q`** to exit and release the camera

***

## 🧪 Adjustable Parameters

You can tune detection performance by adjusting:

*   Camera resolution (`width`, `height`)
*   FPS (`CAP_PROP_FPS`)
*   Detection parameters in:
    ```python
    detectMultiScale(framegray, 1.3, 5)
    ```
    *   Scale factor
    *   Minimum neighbors

***

## 📝 Notes

*   Grayscale conversion improves speed and accuracy
*   Haar Cascades work best with **frontal faces**
*   Lighting conditions affect detection quality
*   This project is ideal as a base for:
    *   Face recognition
    *   Eye detection
    *   Emotion detection
    *   Access control systems

***

## 📄 Author

**Ra‑Jo**
