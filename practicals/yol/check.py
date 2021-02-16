import cv2

TEST_CAMERA = False

def test_yolo():

    _ = cv2.dnn.readNet("yolov3-tiny.weights", "yolov3-tiny.cfg")
    with open("coco.names", "r") as f:
        classes = [ line.strip() for line in f.readlines() ]
    print("Number of classes:\t{}".format(len(classes)))
    [ print(cl) for cl in classes[:5] ]
    print("...")


def test_camera():

    cap = cv2.VideoCapture(0)

    while True:
        _, frame = cap.read()
        cv2.imshow("Image", frame)
        key = cv2.waitKey(1)
        if key == 27:
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    test_yolo()
    if TEST_CAMERA:
        test_camera()
    exit(0)
