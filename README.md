# MantisGestures
MantisGestures provides an alternative to Mantis' usual mouse-centered UI, with the goal of more intuitive
integration with VR in mind. As a proof of concept, the project features hand gesture controls
from outside the Mantis platform. 

MantisGestures requires the pyautogui, mediapipe, and opencv2 (also known as opencv-python for MacOS) libraries. You should also grant it access to your key and webcam for gesture recognition and control.

To run the project, simply run gestures.py.

Gestures list:

- Pinch: Zoom (upwards after pinch is to zoom in, and downwards after pinch is to zoom out)

- Peace Sign: Drag map around x and y axes.

- Close hand: Rotate map around z axis.

- Pinky up: Select (equivalent to mouse's left click).
