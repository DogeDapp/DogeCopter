import time

class Logger(object):
    """log to file"""

    def __init__(self, filename):
        self.filename = filename
        self.log = ""

    def appendStringToLogBuffer(self, value):
        self.log = self.log + str(value)

    def appendLineToLog(self, value):
        f = open(self.filename, "w")
        f.write(self.log + self.getTimestamp() + str(value) + "\n")

    def writeLogToFile(self):
        f = open(self.filename, "w")
        f.write(self.getTimestamp() + self.log)

    def getTimestamp(self):
        return "DOGELOG: " + time.strftime("%H:%M:%S") + ": "

    

