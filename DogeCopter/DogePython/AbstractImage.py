import abc
import numpy as np

class AbstractImage(object):
    """Represents an abstract base class (abc) defining the methods we expect an image to provide"""

    def __init__(self):
        """ setup initial state here """

    def GetImagePixelsAs2DArray(self):

        res = type(np.array([1,2,3]))
        """someData = np.zeros(3,3)"""
        print(res);



