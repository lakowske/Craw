import cv

class LaplaceFrameHandler:
    """LaplaceFrameHandler takes a frame and applies the laplace
    transformation.  It then passes the frame to the next FrameHandler"""
    def __init__(self, frameHandler):
        self.frameHandler = frameHandler

    def handleFrame(self, frame):
        # Sobel operator
        dst = cv.CreateMat(frame.height, frame.width, cv.CV_32FC1)
        cv.Laplace(frame, dst)
        self.frameHandler.handleFrame(dst)
