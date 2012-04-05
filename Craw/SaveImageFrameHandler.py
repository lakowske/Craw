import os, cv, time

class SaveImageFrameHandler:
    """SaveImageFrameHandler takes a frame and saves it to the
    path designated by the frame builder"""
    def __init__(self, pathBuilder):
        self.pathBuilder = pathBuilder

    def handleFrame(self, frame):
        self.imagePath = self.pathBuilder.getPath()
        cv.SaveImage(self.imagePath, frame)

    def getLastImagePath(self):
        return self.imagePath
