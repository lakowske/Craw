import cv

class CaptureCurrentFrameStrategy:
    """CaptureCurrentFrameStrategy advances the frame buffer the given
    amount and then returns the next frame."""
    def __init__(self, frameBufferAdvanceAmount=5):
        self.advanceAmount = frameBufferAdvanceAmount

    def captureFrame(self, capture):
        lastValid = None;
        frames = 0

        while frames < self.advanceAmount:
            img = cv.QueryFrame(capture)
            frames = frames + 1
            if not img:
                continue
            lastValid = img

        img = cv.QueryFrame(capture)
        if not img:
            return lastValid
        return img
