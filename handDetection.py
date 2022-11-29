import cv2
import numpy

def findSubject(cascade, image):
    subjects = cascade.detectMultiScale(image, 1.1, 4)
    allSubjects = []
    for (x, y, w, h) in subjects:
        allSubjects.append((x, y, w, h))

    return allSubjects