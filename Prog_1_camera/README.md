# Open Camera with OpenCV (Python)

## 📌 Description

This project uses **Python** and **OpenCV** to:

*   Open the computer’s **default camera**
*   Display the live video stream in a window
*   Close the camera stream by pressing **`q`**

It is a basic example for learning **computer vision** and **camera handling** in Python.

***

## 🧰 Requirements

*   Computer with a webcam
*   **Python 3.x**
*   **OpenCV (cv2)** library

***

## 📦 Installation

Install OpenCV if it is not already installed:

```bash
pip install opencv-python
```

***

## ⚙️ How It Works

1.  Opens the default camera (`VideoCapture(0)`)
2.  Continuously reads frames from the camera
3.  Displays the frames in a window named **"Yo\_World"** you can change if you want
4.  Waits for user input
5.  Stops the program when the **`q` key** is pressed
6.  Releases the camera and closes all windows properly

***

## ▶️ How to Use

1.  Connect a webcam to your computer
2.  Open the Python script
3.  Run the script:
    ```bash
    python camera.py
    ```
4.  A window showing the live camera feed will open
5.  Press **`q`** on your keyboard to exit

***

## 📝 Notes

*   `VideoCapture(0)` selects the default camera
    *   Try `1` or `2` if you have multiple cameras
*   Make sure no other application is using the camera
*   This script is useful as a base for:
    *   Face detection
    *   Object detection
    *   Video recording
    *   Image processing projects

***

## 📄 Author

Ra-Jo

