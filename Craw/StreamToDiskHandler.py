
class StreamToDiskHandler:
    """Streams frame data to a file"""
    def __init__(self, file="./tmp/mjpgstream2.mjpg"):
        self.file = file
        self.fileObject = open(file, 'wb');
        
    def handleFrame(self, frameData):    
        self.fileObject.write(frameData)