import cv
import time

class CameraCapture:
    """CameraCapture opens a camera for capture and passes
    the camera capture context object to a frame handler"""
    def __init__(self, captureStrategy):
        self.captureStrategy = captureStrategy

    def capture(self, frameHandler):
        self.captureObject = cv.CaptureFromCAM(0)
        frame = self.captureStrategy.captureFrame(self.captureObject)
        frameHandler.handleFrame(frame)
        del(self.captureObject)
