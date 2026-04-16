# Fast Camera Access with OpenCV (Python)

## 📌 Description

This project uses **Python** and **OpenCV** to open a webcam **faster and more efficiently** by explicitly controlling camera parameters such as:

*   Resolution (width & height)
*   Frames Per Second (FPS)
*   Video codec (MJPG)
*   DirectShow backend (Windows)

This approach improves camera startup speed and overall performance compared to a basic camera initialization.

***

## 🧰 Requirements

*   Computer with a webcam
*   **Python 3.x**
*   **OpenCV (cv2)** library
*   Windows OS (uses `CAP_DSHOW` for DirectShow)

***

## 📦 Installation

Install OpenCV if not already installed:

```bash
pip install opencv-python
```

***

## ⚙️ How It Works

1.  Opens the camera using **DirectShow** for faster access
2.  Sets the video resolution to **640 × 360**
3.  Sets the camera frame rate to **30 FPS**
4.  Forces the **MJPG codec** for better performance
5.  Continuously captures and displays frames
6.  Exits cleanly when the **`q` key** is pressed

***

## ▶️ How to Use

1.  Ensure your webcam is connected
2.  Open the Python script
3.  Run the script:
    ```bash
    python fast_camera.py
    ```
4.  A window named **"TheEnginneer"** will appear with the live camera feed
5.  Press **`q`** to close the window and release the camera

***

## 🧪 Adjustable Parameters

You can modify the following values to suit your needs:

*   `width` → camera resolution width
*   `height` → camera resolution height
*   `CAP_PROP_FPS` → frames per second
*   Codec (`MJPG`) → improves speed and reduces latency

***

## 📝 Notes

*   `cv2.CAP_DSHOW` is recommended on **Windows** for faster camera initialization
*   MJPG reduces CPU usage compared to raw formats
*   If the camera does not open:
    *   Try changing the camera index (`0`, `1`, `2`)
    *   Ensure no other application is using the webcam

***

## 📄 Author

Ra‑Jo

