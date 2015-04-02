__author__ = 'Alex'

import cv2
import picamera
import picamera.array

fgbg = cv2.BackgroundSubtractorMOG(25, 6, 0.9, 1)

with picamera.PiCamera() as camera:
    with picamera.array.PiRGBArray(camera) as stream:
        camera.resolution = (320, 240)

        while True:
            camera.capture(stream, 'bgr', use_video_port=True)
            # stream.array now contains the image data in BGR order

            fgmask = fgbg.apply(stream.array)
            cv2.imshow('frame', fgmask)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            # reset the stream before the next capture
            stream.seek(0)
            stream.truncate()

        cv2.destroyAllWindows()