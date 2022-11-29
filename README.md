Simple script to detect where a hand is pointing relative to the camera

<b><h1>Summary and description:</h1></b>
The script fingerFinder.py includes multiple functions for different tasks, as specified in the according comments near them. This program takes each index finger it finds, no matter how many hands are in the frame, and for each hand gets the average location of the knuckles (averaging them out). It then calculates the direction of this average point relative to the base of the index finger, outputting a value into the variable "direction" for each finger. The script also draws a helpful line displaying the direction of the pointing, as well as showing the direction as a tuple next to the finger. It does so for each hand in the frame.

<b><h1>Dependencies:</h1></b>
<em>
- OpenCV
- Mediapipe
- Numpy
</em>

<b><h1>Illustrative screenshot:</h1></b>
![Alt text](IllustrativeScreenshot.png "Optional Title")