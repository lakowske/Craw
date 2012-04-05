import os

class Resources:
    """A utiltity class that returns the resource directory given a
    this module path.  Useful when working with mod_apache as well
    as in other contexts"""
    def __init__(self, modulePath):
        self.modulePath = modulePath
        self.moduleDir = os.path.dirname(modulePath) + "/"

    def getResourcesDirectory(self):
        return self.moduleDir + "../resources/"

