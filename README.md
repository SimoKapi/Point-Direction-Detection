Simple script to detect where a hand is pointing relative to the camera

# Summary and description:
The script fingerFinder.py includes multiple functions for different tasks, as specified in the according comments near them. This program takes each index finger it finds, for a maximum of two hands, and for each hand gets the average location of the knuckles (averaging them out). It then calculates the direction of this average point relative to the base of the index finger, outputting a value into the variable "direction" for each finger. The script also draws a helpful line displaying the direction of the pointing, as well as showing the direction as a tuple next to the finger. It does so for each hand in the frame.

# Dependencies:
- _OpenCV_
- _Mediapipe_
- _Numpy_

# Preview screenshot:
![Preview](IllustrativeScreenshot.png "Optional Title")