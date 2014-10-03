import time
from time import sleep
import Mathinator as Mathinator

class LocationManipulator(object):
    """moves the quad and shit"""


    def __init__(self, v, ratio, brakeDuration):
        self.v = v
        self.ratio = ratio
        self.brakeDuration = brakeDuration
        self.centrePoint = 1515

    def move(self, x, y):
               
        unitx, unity, sleeptime = Mathinator.createUnitVector(x, y, sleep)

        dx = unitx * ratio
        dy = unity * ratio

        self.moveToLocation(dx, dy, sleeptime)
        #v.channel_override = {"1" : int(1515 - dx), "2": int(1515 - dy)}

        self.cancelMovement(unitx, unity) # SHOULD THESE BE UNITX and Y? or DX and DY?
        #v.channel_override = {"1" : int(1515 + dx), "2": int(1515 + dy)}

        self.clearOverrride()        

    def moveToLocation(self, x, y, duration):

        dx = self.centrePoint - x
        dy = self.centrePoint - y
        self.sendCommand(dx, dy, duration)

    def cancelMovement(self, x, y):

        dx = self.centrePoint + x
        dy = self.centrePoint + y
        self.sendCommand(dx, dy, self.brakeDuration)
    
    def sendCommand(self, dx, dy, duration):

        v.channel_override = { "1": dx, "2": dy }
        v.flush()
        sleep(duration)

    def clearOverrride(self):

        v.channel_override = { "1": 0, "2": 0 }
        v.flush()
        sleep(brakeDuration)  
