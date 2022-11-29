import cv2
import mediapipe as mp

mp_Hands = mp.solutions.hands
hands = mp_Hands.Hands()
mpDraw = mp.solutions.drawing_utils
finger_coord = [(0, 6), (12, 10), (16, 14), (20, 18)]
thumb_coord = (4, 2)

"""Function to get coordinates of fingers"""
def getHandCoords(multiLandMarks, img):
    handList = []
    for handLms in multiLandMarks:
        mpDraw.draw_landmarks(img, handLms, mp_Hands.HAND_CONNECTIONS)
        for idx, lm in enumerate(handLms.landmark):
            h, w, c = img.shape
            cx, cy = int(lm.x * w), int(lm.y * h)
            handList.append((cx, cy))

    for point in handList:
        cv2.circle(img, point, 10, (255, 0, 0), cv2.FILLED)
    
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

            for point in handList:
                cv2.circle(img, point, 10, (255, 0, 0), cv2.FILLED)

            upCount = countFingers(handList)

            cv2.putText(img, str(upCount), (150, 150), cv2.FONT_HERSHEY_PLAIN, 12, (0, 255, 0), 12)

        cv2.imshow("# of fingers:", img)
        cv2.waitKey(1)

if __name__ == "__main__":
    main()
