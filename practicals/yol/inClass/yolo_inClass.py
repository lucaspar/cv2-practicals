import cv2
import numpy as np
import time

# Load YOLOv3 model
net = cv2.dnn.readNet("yolov3-tiny.weights", "yolov3-tiny.cfg")

# Download YOLOv3 weights at: https://pjreddie.com/media/files/yolov3.weights
# net = cv2.dnn.readNet("yolov3.weights", "yolov3.cfg")

classes = []
with open("coco.names", "r") as f:
    classes = [line.strip() for line in f.readlines()]
print("Number of classes:",len(classes))
print(classes)

# Get the output layers of our YOLO model
layer_names = net.getLayerNames()
output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]

# Loading the camera
cap = cv2.VideoCapture(0)

# Font and random colors useful later when displaying the results
font = cv2.FONT_HERSHEY_PLAIN
colors = np.random.uniform(0, 255, size=(len(classes), 3))


while True:
    starting_time = time.time()

    _, frame = cap.read()
    height, width, channels = frame.shape


    '''
    *** Step 1: normalize input frame: use cv.dnn.blobFromImage(image[, scalefactor[, size[, mean[, swapRB[, crop[, ddepth]]]]]] to create a "blob" from image.
    Hints:
    -- scale the frame to something small, e.g. (220,220), for YOLOv3-tiny
    -- scale the frame to (320,320) for YOLOv3 
    -- scale value of input images to the 0-1 range (from 0-255 range)
    -- we do not subtract mean from input images
    -- we need to swap R and B channels
    -- we don't need to crop after resize
    
    blob = ...

    '''



    '''
    *** Step 2: use cv.dnn_Net.setInput(blob[, name[, scalefactor[, mean]]]) to put your frame on the network's input.
    Hint:
    -- we no longer need to normalize the brightness
    
    '''



    '''
    *** Step 3: use net.forward() to predict the outputs on the "output_layers"

    outputs = ...

    '''



    '''
    *** Step 4: The detection is done! The only thing to do is to display the results. 
    
    Hints:

    Start with these lines:

    class_ids = []
    confidences = []
    boxes = []

    for out in outputs:
        for detection in out:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]

            Now for this particular object we have its class ID and confidence. 
            But we want to ignore objects with low detection confidence. Thus, in the next lines 
            process only those objects that have confidence higher than some threshold (e.g., 0.2).

            ...

            We may now calculate its box coordinates (x,y,w,h) multiplying values in "detection" vector by the frame width and height:
    
            detection[0] corresponds to X center
            detection[1] corresponds to Y center
            detection[2] corresponds to the box width, and 
            detection[3] corresponds to the box height

            ...

            Once ready, append information about this object to the list of all detected objects in this frame:

            boxes.append([x, y, w, h])
            confidences.append(float(confidence))
            class_ids.append(class_id)
    
    '''



    '''
    *** Step 5: A single object can be represented by multiple boxes. We can remove this "noise"
    by using non-maximum suppression algorithm, implemented as:
    cv.dnn.NMSBoxes(boxes, confidences, confThreshold, nmsThreshold[, eta[, top_k]]	)

    Hints:
    -- use the same "confThreshold" as above
    -- experiment with "nmsThreshold" (you can start with 0.4)

    indices = cv.dnn.NMSBoxes(...

    '''
    


    '''
    Step 6: Display boxes and class labels on the screen.

    Start with these lines:

    for i in range(len(boxes)):
        if i in indices:
        
        Hints:
        -- boxes' indices are in boxes[i]
        -- str(classes[class_ids[i]]) will give you the class label
        -- confidences[i] will give you the confidence score
        -- and you can use colors[class_ids[i]] for a box color
        
        Use "cv2.rectangle" and "cv2.text" to add the detection results to the "frame"

    '''

    # We can also display the FPS:
    fps = 1 / (time.time() - starting_time)
    cv2.putText(frame, "FPS: " + str(round(fps, 2)), (10, 50), font, 3, (0, 0, 0), 3)

    cv2.imshow("Image", frame)
    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()