import cv2

def show_webcam(mirror=False, flip_code=1):
    cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    while True:
        ret_val, img = cam.read()
        cv2.imshow('', img)
        if cv2.waitKey(1) == 27: 
            break  # esc to quit
    cv2.destroyAllWindows()
    cam.release()  # Release the camera resource

def display_cam():
    window_position = (100, 100)
    show_webcam(mirror=True)
