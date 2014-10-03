from droneapi.lib import VehicleModule
from pymavlink import mavutil
import time
from time import sleep
import math
import DogeCopter as DogeCopter

DogeCopter.setupConnection()

count = 0;
flag = True;
initial = 0;
headingTaken = False

canPause = True;

def angle(a , i):
    a_d = math.degrees(a) + 180;
    i_d = math.degrees(i) + 180;

    diff = a_d - i_d;

    if(diff < 0):
        diff = diff + 360;

    return diff



while(True):
    #print(v.channel_readback["6"]);
    channel_6 = v.channel_readback["6"];

    if(channel_6 > 1500):

        if(headingTaken == False):
            headingTaken = True;
            initial = v.attitude.yaw;

        log = time.strftime("%H:%M:%S:%MS");

        channel_8 = v.channel_readback["8"];
        channel_8 = channel_8 - 969; #2075

        ratio = float(float(channel_8) / float(2075/969));
        ratio = 1 + int(ratio * 4);

        log = log + " ratio: " + str(ratio);

        yaw = v.attitude.yaw;
        diff = angle(yaw, initial);

        if(diff > 170 and diff < 220 and flag == True):
            count = count + 1;
            flag = False;

        elif (diff < 20 and flag == False):
            count = count +1;
            flag = True;

        log = log + "\t Flag: " + str(flag) + "\t Count" + str(count) + "\t Diff: " + str(diff)
        amount = float(float(50) * ratio)
        
        if(count == 4 and canPause == True):
            v.channel_override = { "4": 0 }; 
            v.flush();
            sleep(4);
            canPause = False;

        if(count == 8):
            v.channel_override = { "4": 0 };
            v.flush();
            break;
        elif(count < 4):
            v.channel_override = { "4": 1515 + int(amount) };
            v.flush();
        elif(count>= 4):
            v.channel_override = { "4": 1515 - int(amount) };
            v.flush();

        log = log + "\n";
        file.write(log);

        v.channel_override = { "4": 0 };
        v.flush();




