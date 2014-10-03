from droneapi.lib import VehicleModule
import Logger as Logger

class DogeCopter(object):
    """dogecopter util methods"""

    def __init__(self):
        self.v;
        self.api;
        self.log = Logger.Logger("DogeCopterLog.txt")

    def setupConnection(self):
        try:
            self.api = local_connect();
            self.v = api.get_vehicles()[0];
            sleep(5)
            self.log.appendLineToLog("Mav proxy enabled")
        except:
            self.log.appendLineToLog("Mav proxy didn't enable properly")



        


