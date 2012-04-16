import cv

class GrayScaleFrameHandler:
    """GrayScaleFrameHandler takes a frame applies hands off a gray scale frame"""
    def __init__(self, frameHandler):
        self.frameHandler = frameHandler

    def handleFrame(self, frame):
        im_gray = cv.CreateImage(cv.GetSize(frame), cv.IPL_DEPTH_8U, 1)
        cv.CvtColor(frame, im_gray, cv.CV_RGB2GRAY)
        self.frameHandler.handleFrame(im_gray)
