import DogeCopter
import LocationManipulator
import Logger

class DogeRace(object):
    """Creates a dogecopter and begins the race route"""

    def __init__(self):

        self.ratio = 7 # as per Richs instructions
        self.brakeDuration = 0.6 # we think this is enough to stop from 1m (approx)

        # map scale should be adjusted for the course.
        # 1 assumes we're moving at 1 m/sec? (one square on the scaled floor plan)
        self.mapScale = 1 

        self.log = Logger.Logger("racelog.txt")
        self.doge = DogeCopter.DogeCopter()
        self.doge.setupConnection()

        self.mover = LocationManipulator.LocationManipulator(self.doge.v, self.ratio, self.brakeDuration)

        self.createRaceRoute()

        self.beginRace()


    def createRaceRoute(self, mapScale):
        
        self.commands = []

        self.commands[0] = [ 0 , 3 ]
        self.commands[1] = [ -1 , 4 ]
        self.commands[2] = [ -1 , 3 ]
        self.commands[3] = [ -2 , 3 ] # possibly more like -1.8
        self.commands[4] = [ -2 , 2 ]
        self.commands[5] = [ -4 , 2 ]
        self.commands[5] = [ -2 , 0 ]

    def beginRace(self):

        count = 1

        for command in self.commands:
            self.log.appendLineToLog("Move " + count + ": " + command[0] + ", " + command[1])
            self.mover.move(command[0], command[1])
            self.log.appendLineToLog("Move " + count + " complete!")

        self.log.appendLineToLog("Race complete! Such won, many moves, wow!)")
        



        



