# Face and Eye Detection with FPS Calculation using OpenCV (Python)

## 📌 Description

This project uses **Python 3** and **OpenCV** to perform **real‑time detection of multiple faces and eyes** using a webcam.

It also **calculates and displays the FPS (Frames Per Second)** to measure the performance of the application in real time.

***

## 🧰 Requirements

*   Computer with a webcam
*   **Python 3.x**
*   **OpenCV (cv2)** library
*   Haar Cascade XML files:
    *   `haarcascade_frontalface_default.xml`
    *   `haarcascade_eye.xml`

***

## 📦 Installation

### Install OpenCV

```bash
pip install opencv-python
```

### Haar Cascade Files

Download the models from the official OpenCV repository and place them in:

    haar/
    ├── haarcascade_frontalface_default.xml
    ├── haarcascade_eye.xml

***

## ⚙️ How It Works

1.  Opens the webcam using **DirectShow (CAP\_DSHOW)** for faster startup (Windows)
2.  Sets camera parameters:
    *   Resolution: **640 × 360**
    *   FPS: **30**
    *   Codec: **MJPG**
3.  Continuously captures frames from the camera
4.  Converts frames to **grayscale** to reduce computation
5.  Detects:
    *   Multiple **faces** in the frame
    *   **Eyes inside detected face regions** (more accurate)
6.  Draws:
    *   Blue rectangles around faces
    *   White rectangles around eyes
7.  Calculates **FPS** using frame processing time
8.  Displays FPS count on the video stream
9.  Stops when the **`q` key** is pressed

***

## ▶️ How to Use

1.  Connect a webcam to your computer
2.  Ensure the Haar Cascade files are in the correct folder
3.  Open the Python script
4.  Run the script:
    ```bash
    python face_eye_fps.py
    ```
5.  A window named **"Yo\_world"** opens and shows:
    *   Detected faces
    *   Detected eyes
    *   Current FPS
6.  Press **`q`** to exit and release the camera

***

## 📊 FPS Calculation

*   FPS is calculated based on the execution time of each loop
*   A smoothing filter is applied:
    *   Helps stabilize FPS display
    *   Avoids rapid fluctuations

The FPS value is displayed in the **top‑left corner** of the video.

***

## 🧪 Adjustable Parameters

You can optimize detection and performance by modifying:

*   Camera resolution (`width`, `height`)
*   FPS (`CAP_PROP_FPS`)
*   Haar detection settings:
    ```python
    detectMultiScale(gray, 1.3, 5)
    ```
    *   Scale factor
    *   Minimum neighbors

***

## 📝 Notes

*   Eye detection is performed only inside detected face regions for better accuracy
*   Good lighting improves detection results
*   Haar Cascades work best with frontal faces
*   This project is a great base for:
    *   Face recognition
    *   Attention tracking
    *   Security systems
    *   Performance benchmarking (FPS)

***

## 📄 Author

**Ra‑Jo**
