import cv

class CaptureCurrentFrameStrategyTillValid:
    """CaptureCurrentFrameStrategyTillValid advances the frame buffer a given
    amount and returns last img.  If the img is not valid, a default
    unavailable image is returned"""
    def __init__(self, unavailableImagePath, frameBufferAdvanceAmount=5):
        self.unavailableImagePath = unavailableImagePath
        self.advanceAmount = frameBufferAdvanceAmount

    def captureFrame(self, capture):
        img = None;
        frames = 0

        while frames < self.advanceAmount:
            img = cv.QueryFrame(capture)
            frames = frames + 1

        if not img:
            img = cv.LoadImage(self.unavailableImagePath)

        return img
