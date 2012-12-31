import urllib

class MJPGHTTPCameraCapture:
    """Opens a connection to a mjpg over http camera"""
        
    def __init__(self, url, readAmount=1024):
        self.url = url
        self.readAmount = readAmount
        self.captureObject = urllib.urlopen(self.url)
                
    def capture(self, frameHandler):
        data = self.captureObject.read(self.readAmount)
        while (data != ""):
            frameHandler.handleFrame(data)
            data = self.captureObject.read(self.readAmount)
        
        
        