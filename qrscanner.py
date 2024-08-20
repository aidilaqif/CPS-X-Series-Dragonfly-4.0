import cv2
from pyzbar.pyzbar import decode
import time

# Iterate through potential camera indices
# for i in range(10):  # Check indices 0 to 9
#     cam = cv2.VideoCapture(i)
#     if cam.isOpened():
#         print(f"Camera found at index {i}")
#         cam.release()

# Check if camera opened successfully
# if not cam.isOpened():
#     print("Error opening video stream or file")
#     exit() # Exit if camera cannot be opened

cam = cv2.VideoCapture(0)

# window reflected when camera is true
cam.set(5, 640) # width = 5, pixel = 640
cam.set(6, 480) # height = 6, pixel = 480

camera = True
while camera == True:
    success, frame = cam.read()

    if success: # Check if a frame was successfully read
        #decode
        for i in decode(frame):
            print(i.type)
            print(i.data.decode('utf-8'))
            time.sleep(6)

        cv2.imshow("OurQR_Code_Scanner", frame)
        cv2.waitKey(3) # capture frame after 3 seconds
    else:
        print("Failed to read frame. Check camera connection.")
        break # Exit loop if reading a frame fails

# Release resources
cam.release()
cv2.destroyAllWindows()