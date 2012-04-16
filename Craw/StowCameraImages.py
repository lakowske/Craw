from CameraCapture import *
from SaveImageFrameHandler import *
from CaptureCurrentFrameStrategy import *
from CaptureCurrentFrameStrategyTillValid import *
from SobelFrameHandler import *
from LaplaceFrameHandler import *
from BlurFrameHandler import *
from GrayScaleFrameHandler import *
from PathBuilder import *
import Resources

"""This module uses the IoC pattern to build and configure objects
used to capture images.  Given the interfaces and implementations,
you can plug in new implementations without changing the rest of the
code base.  Thus satisfy the DRY principle and the O in SOLID"""

#Construct our objects and inject our dependencies.
resources = Resources.Resources(Resources.__file__)
captureCurrentFrameStrategyTillValid = CaptureCurrentFrameStrategyTillValid(resources.getResourcesDirectory() + "noimage.png")
cameraCapture = CameraCapture(captureCurrentFrameStrategyTillValid)
pathBuilder = PathBuilder()
saveImageFrameHandler = SaveImageFrameHandler(pathBuilder)
sobelFrameHandler = SobelFrameHandler(saveImageFrameHandler)
laplaceFrameHandler = LaplaceFrameHandler(saveImageFrameHandler)
blurFrameHandler = BlurFrameHandler(laplaceFrameHandler)
grayScaleFrameHandler = GrayScaleFrameHandler(blurFrameHandler)

def capture():
    cameraCapture.capture(grayScaleFrameHandler)

