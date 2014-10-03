import numpy as np

class Mathinator(object):
    """does maths and ting"""


    def getHypotonuse(self, x, y):
        h = np.sqrt(x * x + y * y)
        return h

    def createUnitVector(self, x, y, speed):
        
            h = np.sqrt(x * x + y * y)  

            sleeptime = h / speed

            unitx = x / h
            unity = y / h

            return unitx, unity, sleeptime

