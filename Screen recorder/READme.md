# 🖥️ Python Screen Recorder

A simple Python-based **screen recording program** that captures the computer screen continuously and saves the captured frames as a video file.

The project uses **PyAutoGUI** for screen capture, **NumPy** for image-array processing, and **OpenCV** for video creation and live preview.

---

## 📌 Introduction

This project demonstrates how a screen recorder can be built using basic image-processing concepts.

Instead of directly recording the screen as a video, the program repeatedly:

1. 📸 Captures a screenshot.
2. 🔢 Converts the screenshot into a NumPy array.
3. 🎨 Converts the image from RGB to BGR.
4. 🎥 Writes the frame into a video file.
5. 👀 Displays the captured frame in a live preview.
6. ⌨️ Checks whether the user pressed `q`.

The process continues until `q` is pressed.

---

## ✨ Features

* 🖥️ Captures the entire screen
* 📸 Continuously takes screenshots
* 🔢 Converts screenshots into NumPy arrays
* 🎨 Converts RGB frames to BGR for OpenCV
* 🎥 Saves captured frames into a video
* 👀 Provides a live preview
* ⌨️ Press `q` to stop recording
* 🧹 Releases OpenCV resources after recording

---

## 🔄 How It Works

The overall process can be represented as:

```text
        🖥️ Screen
            │
            ▼
   📸 PyAutoGUI Screenshot
            │
            ▼
     🔢 NumPy Array
            │
            ▼
       RGB → BGR
            │
            ▼
     🎥 VideoWriter
            │
            ▼
    📁 Recording.mjpg
```

At the same time, OpenCV displays the current frame:

```text
Screenshot
    │
    ├──────────────► Video File
    │
    └──────────────► Live Preview
```

---

## 🛠️ Tech Stack

| Technology   | Purpose                                |
| ------------ | -------------------------------------- |
| 🐍 Python    | Main programming language              |
| 📸 PyAutoGUI | Captures screenshots                   |
| 🔢 NumPy     | Converts images into arrays            |
| 🎥 OpenCV    | Processes frames and creates the video |

---

## 📦 Installation

Install the required Python libraries:

```bash
pip install pyautogui numpy opencv-python
```

Or install them individually:

```bash
pip install pyautogui
pip install numpy
pip install opencv-python
```

---

## ⚙️ Configuration

The program currently uses the following settings:

### Resolution

```python
resolution = (1920, 1080)
```

The intended recording resolution is:

```text
Width  → 1920 pixels
Height → 1080 pixels
```

### Codec

```python
codec = cv2.VideoWriter_fourcc(*"MJPG")
```

The project uses the **MJPG** codec.

### Frame Rate

```python
fps = 15
```

The video is configured for **15 FPS**.

---

## 🎥 VideoWriter

The program creates a video writer:

```python
out = cv2.VideoWriter(
    "Recording.mjpg",
    codec,
    fps,
    resolution
)
```

This tells OpenCV:

| Setting     | Value            |
| ----------- | ---------------- |
| Output file | `Recording.mjpg` |
| Codec       | MJPG             |
| FPS         | 15               |
| Resolution  | 1920 × 1080      |

The `VideoWriter` receives one frame at a time through:

```python
out.write(frame)
```

---

## 🖥️ Live Preview

The program creates a resizable OpenCV window:

```python
cv2.namedWindow("Live", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Live", 480, 270)
```

The actual recording remains configured for `1920 × 1080`, while the preview window is displayed at:

```text
480 × 270
```

This makes the live preview easier to view without occupying the entire screen.

---

## 📸 Screen Capture

PyAutoGUI captures the current screen:

```python
img = pyautogui.screenshot()
```

The result is a PIL Image.

It is then converted into a NumPy array:

```python
frame = np.array(img)
```

This allows OpenCV to process the screenshot as an image frame.

---

## 🎨 RGB to BGR Conversion

PyAutoGUI provides the screenshot in **RGB** format.

OpenCV commonly expects images in **BGR** format.

Therefore, the program converts the frame:

```python
frame = cv2.cvtColor(
    frame,
    cv2.COLOR_RGB2BGR
)
```

Without this conversion, the colors may appear incorrectly when processed or displayed by OpenCV.

---

## 🔁 Recording Loop

The main recording process runs inside:

```python
while True:
```

Every iteration performs these operations:

```text
1. Take screenshot
       ↓
2. Convert to NumPy array
       ↓
3. RGB → BGR
       ↓
4. Write frame to video
       ↓
5. Display live preview
       ↓
6. Check for 'q'
       ↓
7. Repeat
```

---

## ⌨️ Stopping the Recording

The program checks for keyboard input using:

```python
cv2.waitKey(1)
```

The returned value is compared with:

```python
ord('q')
```

Therefore, pressing **`q`** stops the recording:

```python
if cv2.waitKey(1) == ord('q'):
    break
```

---

## 🧹 Resource Cleanup

After the loop ends, the video writer is released:

```python
out.release()
```

This finalizes the video file and releases the resources used by the writer.

The OpenCV windows are then closed:

```python
cv2.destroyAllWindows()
```

---

## 🔄 Program Flow

```text
             ┌─────────────┐
             │    Start    │
             └──────┬──────┘
                    │
                    ▼
        Import Required Libraries
                    │
                    ▼
       Set Resolution / Codec / FPS
                    │
                    ▼
          Create VideoWriter
                    │
                    ▼
           Create Preview Window
                    │
                    ▼
            ┌───────────────┐
            │ Take Screenshot│
            └───────┬───────┘
                    │
                    ▼
           Convert to NumPy
                    │
                    ▼
              RGB → BGR
                    │
                    ▼
             Write Frame
                    │
                    ▼
            Show Live Preview
                    │
                    ▼
             Pressed `q`?
              /          \
            No            Yes
            │              │
            │              ▼
            │         Stop Loop
            │              │
            └──────►       ▼
                    Release Writer
                           │
                           ▼
                    Destroy Windows
                           │
                           ▼
                          End
```

---

## 🧩 Important Functions

| Function                   | Purpose                            |
| -------------------------- | ---------------------------------- |
| `pyautogui.screenshot()`   | Captures the screen                |
| `np.array()`               | Converts screenshot to NumPy array |
| `cv2.cvtColor()`           | Converts RGB to BGR                |
| `cv2.VideoWriter_fourcc()` | Creates codec information          |
| `cv2.VideoWriter()`        | Creates video writer               |
| `cv2.namedWindow()`        | Creates preview window             |
| `cv2.resizeWindow()`       | Resizes preview window             |
| `cv2.imshow()`             | Displays the current frame         |
| `cv2.waitKey()`            | Detects keyboard input             |
| `out.write()`              | Writes a frame to the video        |
| `out.release()`            | Releases video writer              |
| `cv2.destroyAllWindows()`  | Closes OpenCV windows              |

---

## 🧠 Concepts Practiced

This project provides practice with:

* 🐍 Python modules
* 📦 External libraries
* 🖥️ Screen capture
* 📸 Image processing
* 🔢 NumPy arrays
* 🎨 RGB and BGR color formats
* 🎥 Video processing
* 🔁 Infinite loops
* ⌨️ Keyboard detection
* 🪟 OpenCV windows
* ⚙️ Video codecs
* 🎞️ Frame rates
* 🧹 Resource management

---

## 💻 Complete Code

```python
import cv2
import pyautogui
import numpy as np

# Specify resolution
resolution = (1920, 1080)

# Specify codec
codec = cv2.VideoWriter_fourcc(*"MJPG")

# Specify framerate
fps = 15

# Create a VideoWriter object
out = cv2.VideoWriter(
    "Recording.mjpg",
    codec,
    fps,
    resolution
)

# Create an empty window
cv2.namedWindow("Live", cv2.WINDOW_NORMAL)

# Resize the window
cv2.resizeWindow("Live", 480, 270)

# Start recording
while True:

    # Take screenshot using PyAutoGUI
    img = pyautogui.screenshot()

    # Convert screenshot to NumPy array
    frame = np.array(img)

    # Convert RGB to BGR
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

    # Write frame to output file
    out.write(frame)

    # Display recording screen
    cv2.imshow("Live", frame)

    # Press q to stop
    if cv2.waitKey(1) == ord("q"):
        break

# Release the video writer
out.release()

# Close all OpenCV windows
cv2.destroyAllWindows()
```

---

## ▶️ How to Run

### 1. Clone the Repository

```bash
git clone <repository-url>
```

### 2. Enter the Project Directory

```bash
cd <project-folder>
```

### 3. Install Dependencies

```bash
pip install pyautogui numpy opencv-python
```

### 4. Run the Program

```bash
python main.py
```

The screen recording will begin immediately.

### 5. Stop Recording

Press:

```text
q
```

The recording will stop and the video file will be finalized.

---

## 📁 Output

After recording, the project generates:

```text
Recording.mjpg
```

The file is created in the current working directory.

---

## ⚠️ Known Limitations

There are no major errors in the current implementation, but there are a few limitations:

### 1. Fixed Resolution

The resolution is hardcoded:

```python
resolution = (1920, 1080)
```

If the actual screen resolution is different, the captured frame dimensions may not match the `VideoWriter` configuration.

### 2. Fixed Frame Rate

The configured frame rate is:

```python
fps = 15
```

The actual screenshot capture speed can depend on system performance.

### 3. Video-Only Recording

The program captures the screen but does **not** record:

* 🎤 Microphone audio
* 🔊 System audio

### 4. No Pause Function

The current version only supports starting and stopping the recording.

### 5. No Region Selection

The entire screen is captured. The user cannot currently select a specific area.

### 6. Output Format

The output uses the MJPG codec and `.mjpg` file extension. Playback compatibility can depend on the media player and installed codecs.

---

## 🚀 Future Improvements

Possible improvements include:

* 🖥️ Automatically detect screen resolution
* 🎯 Record a selected screen region
* ⏯️ Add pause/resume functionality
* ⏱️ Add recording duration
* 🎤 Add microphone recording
* 🔊 Add system audio recording
* 🎞️ Support additional video formats
* ⚙️ Allow users to select FPS
* 📂 Allow users to choose the output location
* ⌨️ Add customizable keyboard shortcuts
* 🖱️ Highlight mouse movement and clicks
* 🖥️ Create a graphical user interface

---

## 📊 Project Structure

```text
Screen-Recorder/
│
├── main.py
├── Recording.mjpg
└── README.md
```

`Recording.mjpg` will be generated after running the program.

---

## 📌 Project Status

🟢 **Completed**

Current version supports:

* ✅ Screen capture
* ✅ Frame conversion
* ✅ RGB → BGR conversion
* ✅ Video creation
* ✅ Live preview
* ✅ `q` key to stop recording
* ✅ Resource cleanup

---

## 🎓 What I Learned

This project demonstrates how a video can be created from a continuous sequence of screenshots.

The fundamental idea is:

```text
Screenshot 1 ─┐
Screenshot 2 ─┤
Screenshot 3 ─┼──► Video
Screenshot 4 ─┤
Screenshot 5 ─┘
```

It provided practical experience with **PyAutoGUI, NumPy, OpenCV, image formats, video codecs, frame rates, and real-time processing**.

---

## 👨‍💻 Author

**Uzair Khan**

GitHub: `khanuzair-f15`

Email: `khanuzair.f15@gmail.com`

---

⭐ If you found this project useful, consider giving the repository a star!
