"""
Install Required Libraries
~ PyAutoGUI: Captures screenshots of the screen.
~ NumPy: Converts screenshots into arrays for processing.
~ OpenCV: Handles video creation and frame processing.


Capture the Screen: The program continuously takes screenshots using PyAutoGUI.
Convert Screenshots to Frames: Each screenshot is converted into a NumPy array that can be processed by OpenCV.
Write Frames to a Video: OpenCV stores the captured frames in a video file using a specified codec and frame rate.
Display Live Preview (Optional): A preview window shows the recording while it is in progress.
Stop Recording: Pressing the q key stops the recording and saves the video.
"""

# Function reference

# cv2.VideoWriter_fourcc(*"XVID") - generates 4-char codec code for video compression format
# cv2.VideoWriter(file, codec, fps, res) - creates video writer object to save frames to file
# cv2.namedWindow(name, WINDOW_NORMAL) - creates resizable display window
# cv2.resizeWindow(name, w, h) - sets window size in pixels
# pyautogui.screenshot() - captures screen, returns PIL Image (RGB)
# np.array(img) - converts PIL Image to NumPy array
# cv2.cvtColor(frame, COLOR_RGB2BGR) - converts RGB to BGR for OpenCV
# out.write(frame) - writes single frame to video file
# cv2.imshow(name, frame) - displays frame in window (live preview)
# cv2.waitKey(1) - waits 1ms for key press, returns key code
# ord('q') - returns ASCII value of 'q' for key comparison
# out.release() - finalizes and closes video file, frees resources
# cv2.destroyAllWindows() - closes all OpenCV windows

# importing the required packages

import cv2
import pyautogui
import numpy as np

# specify resolution
resolution = (1920, 1080)

# specify codec
codec = cv2.VideoWriter_fourcc(*"MJPG")  # we have to specify a 4-byte code (such as XVID, MJPG, X264, etc.)

# specify framerate
fps = 15

# Creating a VideoWriter object
out = cv2.VideoWriter("Recording.mjpg", codec, fps, resolution)

# Create an Empty window
cv2.namedWindow("Live", cv2.WINDOW_NORMAL)

# resize the window
cv2.resizeWindow("Live", 480, 270)

"""
Now, let's start recording our screen. We will be running an infinite loop and in each iteration of the loop, 
we will take a screenshot and write it to the output file with the help of the video writer.
"""

while True:
    # taking screenshot using pyautogui
    img = pyautogui.screenshot()

    # convert the ss to numpy array
    frame = np.array(img)

    # convert frame from RGB to BGR
    # for cv2 processing
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

    # write it to output file
    out.write(frame)

    # Optional: Display the recording screen
    cv2.imshow('Live', frame)

    if cv2.waitKey(1) == ord('q'):
        break

"""
After everything is done, we will release the writer and destroy all windows opened by OpenCV.
"""

# release the video writer
out.release()

cv2.destroyAllWindows()
