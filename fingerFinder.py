import cv2
import mediapipe as mp
import numpy

mp_Hands = mp.solutions.hands
hands = mp_Hands.Hands()
mpDraw = mp.solutions.drawing_utils
finger_coord = [(0, 6), (12, 10), (16, 14), (20, 18)]
thumb_coord = (4, 2)

"""Function to get coordinates of fingers"""
def getHandCoords(multiLandMarks, img):
    handList = []
    for handLms in multiLandMarks:
        #mpDraw.draw_landmarks(img, handLms, mp_Hands.HAND_CONNECTIONS)
        for idx, lm in enumerate(handLms.landmark):
            h, w, c = img.shape
            cx, cy = int(lm.x * w), int(lm.y * h)
            handList.append((cx, cy))
    
    return handList

"""Function to count number of raised fingers"""
def countFingers(handList):
    upCount = 0
    for coordinate in finger_coord:
        if handList[coordinate[0]][1] < handList[coordinate[1]][1]:
            upCount += 1
    if handList[thumb_coord[0]][0] > handList[thumb_coord[1]][0]:
        upCount += 1

    return upCount

"""Main function"""
def main():
    vidCap = cv2.VideoCapture(0)

    while True:
        success, img = vidCap.read()
        RGB_image = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = hands.process(RGB_image)
        multiLandMarks = results.multi_hand_landmarks

        if multiLandMarks:
            handList = getHandCoords(multiLandMarks, img)

            #tip of index: 8 if 1 hand / 29 & 8 if 2 hands
            #base of index: 5 if 1 hand / 26 & 5 if 2 hands
            """for point in handList:
                cv2.circle(img, point, 10, (255, 0, 0), cv2.FILLED)
                cv2.putText(img, str(handList.index(point)), point, cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 1)"""
            #cv2.circle(img, handList[8], 10, (255, 0, 0), cv2.FILLED)

            indexBase = 5
            indexTip = 8
            pointSet = []

            #Get points of all knuckles on index finger
            for i in range(indexBase, indexTip + 1):
                #cv2.circle(img, handList[i], 10, (255, 0, 0), cv2.FILLED)
                pointSet.append(handList[i])

            #Calculate list of all xs and ys in pointSet
            xs = []
            ys = []
            for tup in pointSet:
                xs.append(tup[0])
                ys.append(tup[1])

            #Get average point from each knuckle on index finger
            avPoint = (int(sum(xs)/len(xs)), int(sum(ys)/len(ys)))

            #Calculate direction of two points
            direction = numpy.subtract(avPoint, handList[indexBase])
            cv2.putText(img, str(direction), handList[indexBase], cv2.FONT_HERSHEY_PLAIN, 2, (185, 232, 255), 2)

            cv2.line(img, handList[indexBase], handList[indexBase] + (direction * 5), (185, 232, 255), 3)

        cv2.imshow("Direction view:", img)
        cv2.waitKey(30)

if __name__ == "__main__":
    main()
