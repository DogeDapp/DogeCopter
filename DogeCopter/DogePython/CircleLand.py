from droneapi.lib import VehicleMode
from pymavlink import mavutil
import time
from time import sleep
import cv2
import numpy as np
import Mathinator

api = local_connect()
v = api.get_vehicles()[0]

cmds = v.commands
cmds.download()
cmds.wait_valid()
v.armed = False
v.flush()

v.armed = True
v.flush()
sleep(5)

print("Starting video")
vc = cv2.VideoCapture(0)

flag = False

dx = 0
dy = 0

print("Starting Dance")
file.open("landing_py_log.txt", "w")

speed = float(5)
gimpfactor = float(2)
enbrakenator = float(1)
ratio = 85

def move(x, y, ratio):
               
        unitx, unity, sleep = Mathinator.createUnitVector(x, y, sleep)

        dx = unitx * ratio
        dy = unity * ratio

        # initial command
        v.channel_override = {"1" : int(1515 + dx), "2": int(1515 + dy)}
        v.flush()

        sleep(sleeptime)

        # counteract
        v.channel_override = {"1" : int(1515 - dx / gimpfactor), "2": int(1515 - dy / gimpfactor)}
        v.flush()

        sleep(enbrakenator)

        # clear
        v.channel_override = { "1": 0, "2": 0 }
        v.flush()

        sleep(enbrakenator)        


while(True):
    channel_6 = v.channel_readback["6"]

    if(channel_6 > 1500):

        rval, frame = vc.read()
        hsv = cv.cvtColour(frame, cv2.COLOR_BGR2HSV)
        channels = cv2.split(hsv)

        lower = np.array([0 , 0, 100], np.uint8)
        higher = np.array([20, 255, 255], np.uint8)

        mask = cv2.inRange(hsv, lower, higher)

        contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        area = 0.0
        maxColour = None
        i = -1
        contour1 = -1

        for contour in contours:
            i = i + 1
            a = cv2.contourArea(contour)
            if a > area:
                area = a
                maxContour = contour
                countourI = i

        log = time.strftime("%H:%M:%S:%MS")
        log = log + " Area:" + str(area)

        if area > 150:
            channel_8 = v.channel_readback["8"]
            channel_8 = channel_8 - 969 #2075

            ratio = float(float(channel_8) / float(2075 / 969))
            ratio = 1 + int(ratio * 20)
            log = log + "\tRatio " + str(ratio)

            m = cv.moments(maxContour)
            cx = int(m['m10'] / m['m00'])
            cy = int(m['m01'] / m['m00'])

            dx = (32 - cx) * ratio
            dy = (32 - cy) * ratio

            log = log + "\tCentre: " + str(cx) + "," + str(cy)
            log = log + "\tOverrride:" + str(int(1515 + dx)) + "," + str(int(1515 + dy))

            # initial command

            v.channel_override = {"1" : int(1515 + dx), "2": int(1515 + dy)}
            v.flush()

            sleep(0.1)

            # counteract
            gimpfactor = float(2)
            v.channel_override = {"1" : int(1515 - dx / gimpfactor), "2": int(1515 - dy / gimpfactor)}
            v.flush()

            sleep(0.1)

            # clear

            v.channel_override = { "1": 0, "2": 0 }
            v.flush()

            sleep(0.1)
        else:

            # attack nearest person
            v.channel_override = {"1" : int(1515 - dx), "2": int(1515 - dy)}
            v.flush()

        log = log + "\n"
        file.write(log)

    else:

        # cancel freakout
        v.channel_override = { "1": 0, "2": 0 }





