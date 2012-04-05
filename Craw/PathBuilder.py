import os

class PathBuilder:
    """Constructs a sequence of paths at the given path directory with the given suffix"""

    def __init__(self, path="./tmp/", suffix=".png"):
        self.path = path
        self.suffix = suffix
        self.count = 0
        #Construct the path if none exists
        if not os.path.isdir(path):
            os.makedirs(path)
        
    def getPath(self):
        newPath = self.path + str(self.count) + self.suffix
        self.count = self.count + 1
        return newPath
