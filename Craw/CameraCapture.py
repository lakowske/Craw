import cv
import time

class CameraCapture:
    """CameraCapture opens a camera for capture and passes
    the camera capture context object to a frame handler"""
    def __init__(self, captureStrategy):
        self.captureStrategy = captureStrategy
        self.captureObject = cv.CaptureFromCAM(0)

    def capture(self, frameHandler):
        frame = self.captureStrategy.captureFrame(self.captureObject)
        frameHandler.handleFrame(frame)

