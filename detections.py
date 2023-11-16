import cv2
import numpy as np
import time
import urllib.request

# Load YOLO file/
net = cv2.dnn.readNet("yolov3.weights", "yolov3.cfg")
classes = []

# replace with camera URL
url='http://192.168.200.101/cam-hi.jpg'

# Load class names from coco file
with open("coco.names", "r") as f:
    classes = f.read().strip().split("\n")


while True:
    # load an image from the camera server
    img_resp=urllib.request.urlopen(url)
    # use numpy to turn the image into an array of values
    imgnp=np.array(bytearray(img_resp.read()),dtype=np.uint8)
    # use openCV to turn the array of values into an openCV image
    frame = cv2.imdecode(imgnp,-1)

    # Run YOLO on the frame
    # Convert the frame to a blob that YOLO can process
    # - frame: the input image frame
    # - 0.00392: scale factor (1/255)
    # - (416, 416): target size of the input blob
    # - (0, 0, 0): mean subtraction values for each channel (BGR)
    # - True: swap Red and Blue channels (OpenCV uses BGR)
    # - crop=False: don't crop the image, resize it

    blob = cv2.dnn.blobFromImage(frame, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
    net.setInput(blob)  # Set the input blob for the neural network
    outs = net.forward(net.getUnconnectedOutLayersNames()) # Forward pass the input blob through the network to get detections

    # Process YOLO output
    for out in outs:
        for detection in out:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > 0.5:  # Filter detections by confidence threshold
                center_x = int(detection[0] * frame.shape[1])
                center_y = int(detection[1] * frame.shape[0])
                width = int(detection[2] * frame.shape[1])
                height = int(detection[3] * frame.shape[0])

                x = int(center_x - width / 2)
                y = int(center_y - height / 2)

                # Draw  box and label on the frame
                cv2.rectangle(frame, (x, y), (x + width, y + height), (0, 255, 0), 2)
                label = f"{classes[class_id]}: {confidence:.2f}"
                cv2.putText(frame, label, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # Display the frame with detections
    cv2.imshow(" DISPLAYING : FRAME |  Detections", frame)
    key = cv2.waitKey(5)  # continue after 5 msec unless a keypress is registered, in which case break out of the loop
    if key==ord('q'):
        print("out")
        break


cv2.destroyAllWindows()
