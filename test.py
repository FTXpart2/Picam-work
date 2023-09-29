from picamera2 import Picamera2, Preview
import time

picam2 = Picamera2()
picam2.start_preview(Preview.NULL)
for x in range(0,10):
    picam2.start_and_capture_file("wes-{}.jpg".format(x) )
    time.sleep(30)