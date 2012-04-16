import cv

class BlurFrameHandler:
    """BlurFrameHandler takes a frame and applies a smooth operation"""
    def __init__(self, frameHandler):
        self.frameHandler = frameHandler

    def handleFrame(self, frame):
        imageBlur = cv.CreateImage(cv.GetSize(frame), frame.depth, frame.nChannels)
        cv.Smooth(frame, imageBlur, cv.CV_BLUR, 3, 3)
        self.frameHandler.handleFrame(imageBlur)
