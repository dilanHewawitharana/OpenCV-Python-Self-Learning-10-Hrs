import cv2
import datetime

cap = cv2.VideoCapture(1)

print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        font = cv2.FONT_HERSHEY_PLAIN
        text = 'Width : ' + str(cap.get(3)) + ' Height : ' + str(cap.get(4))
        date_time = str(datetime.datetime.now())
        frame = cv2.putText(frame, text, (10, 15), font, 1, (0, 255, 255), 2, cv2.LINE_AA)
        frame = cv2.putText(frame, date_time, (10, 35), font, 1, (0, 255, 255), 2, cv2.LINE_AA)

        cv2.imshow('Output', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()


