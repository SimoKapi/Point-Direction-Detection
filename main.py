import cv2
import mediapipe as mp
import handDetection

from handDetection import findSubject

def findSubject(cascade, image):
    subjects = cascade.detectMultiScale(image, 1.2, 5)
    allSubjects = []
    for (x, y, w, h) in subjects:
        allSubjects.append((x, y, w, h))

    return allSubjects

def main():
    #faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    palmCascade = cv2.CascadeClassifier("palm.xml")
    vidCap = cv2.VideoCapture(0)

    while True:
        _, img = vidCap.read()
        grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        subjects = findSubject(palmCascade, grayImg)

        for subject in subjects:
            x, y, w, h = subject
            cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

        cv2.imshow("Image", img)
        k = cv2.waitKey(30) & 0xff
        if k == 27:
            break
    vidCap.release()


if __name__ == "__main__":
    main()
