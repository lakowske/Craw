import cv

class SobelFrameHandler:
    """SobelFrameHandler takes a frame and applies the sobel
    transformation.  It then passes the frame to the next FrameHandler"""
    def __init__(self, frameHandler):
        self.frameHandler = frameHandler

    def handleFrame(self, frame):
        # Sobel operator
        dstSobel = cv.CreateMat(frame.height, frame.width, cv.CV_32FC1)
        cv.Sobel(frame, dstSobel, 1, 1, 3)
        self.frameHandler.handleFrame(dstSobel)
