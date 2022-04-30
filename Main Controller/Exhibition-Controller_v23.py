# Version | 20.00
# License | WTFPL http://www.wtfpl.net/

# Code written and designed by Elliott Hall
# Project | The Museum

# www.elliotthall.co.uk
# @elliotth30 / @obscure_design

#   Importing Repositories
from ast import While
from omxplayer.player import OMXPlayer
from pathlib import Path
from time import sleep
import requests

import multiprocessing
import subprocess
from subprocess import run

import os
import os.path # used for file lookup confirmation

import vlc

#   Declaring Trigger URL's
#       Lighting
P1_ON = 'http://192.168.4.1/P1_ON?'
P1_OFF = 'http://192.168.4.1/P1_OFF?'
P2_ON = 'http://192.168.4.1/P2_ON?'
P2_OFF = 'http://192.168.4.1/P2_OFF?'
P3_ON = 'http://192.168.4.1/P3_ON?'
P3_OFF = 'http://192.168.4.1/P3_OFF?'
#       Features
P1_X_ON = 'http://192.168.4.1/P1_X_ON?'
P1_X_OFF = 'http://192.168.4.1/P1_X_OFF?'
P2_X_ON = 'http://192.168.4.1/P2_X_ON?'
P2_X_OFF = 'http://192.168.4.1/P2_X_OFF?'
P3_X_ON = 'http://192.168.4.1/P3_X_ON?'
P3_X_OFF = 'http://192.168.4.1/P3_X_OFF?'

#   Inital Start-Up. Turning Off All.
#       Lighting
requests.get(P1_OFF, timeout=0.50)
sleep(0.2)
requests.get(P2_OFF, timeout=0.50)
sleep(0.2)
requests.get(P3_OFF, timeout=0.50)
sleep(0.2)
#       Features
requests.get(P1_X_OFF, timeout=0.50)
sleep(0.2)
requests.get(P2_X_OFF, timeout=0.50)
sleep(0.2)
requests.get(P3_X_OFF, timeout=0.50)
sleep(0.2)

def video_play_1():
    subprocess.run('vlc --fullscreen --deinterlace-mode=auto 1s.mp4', shell=True)

def video_play_3():
    subprocess.run('vlc --fullscreen --deinterlace-mode=auto 2.mp4', shell=True)

def video_play_2():
    subprocess.run('vlc --fullscreen --deinterlace-mode=auto 3s.mp4', shell=True)

def video_kill():
    subprocess.run('killall -9 vlc', shell=True)

def video_script(num): 
    if num == 1:
        print("1")
        video_process = multiprocessing.Process(target=video_play_1)
        video_process.start()
        sleep_1 = 1
        sleep_2 = 90
        sleep_3 = 30
        sleep_4 = 103
        op_1 = 'http://192.168.4.1/P1_ON?'
        op_2 = 'http://192.168.4.1/P1_X_ON?'
        op_3 = 'http://192.168.4.1/P1_X_OFF?'
        op_4 = 'http://192.168.4.1/P1_OFF?'

    elif num == 2:
        print("2")
        video_process = multiprocessing.Process(target=video_play_2)
        video_process.start()
        sleep_1 = 1
        sleep_2 = 5
        sleep_3 = 5
        sleep_4 = 89
        op_1 = 'http://192.168.4.1/P2_ON?'
        op_2 = 'http://192.168.4.1/P2_X_ON?'
        op_3 = 'http://192.168.4.1/P2_X_OFF?'
        op_4 = 'http://192.168.4.1/P2_OFF?'

    elif num == 3:
        print("3")
        video_process = multiprocessing.Process(target=video_play_3)
        video_process.start()
        sleep_1 = 1
        sleep_2 = 5
        sleep_3 = 5
        sleep_4 = 122
        op_1 = 'http://192.168.4.1/P3_ON?'
        op_2 = 'http://192.168.4.1/P3_X_ON?'
        op_3 = 'http://192.168.4.1/P3_X_OFF?'
        op_4 = 'http://192.168.4.1/P3_OFF?'

    else:
        print("You've Fucked it somewhere along the way my friend. sorry.")
    
    print(op_1, op_2, op_3, op_4)
    run('vcgencmd display_power 1', shell=True)
    sleep(sleep_1) # - Allowing video to render.
    requests.get(op_1, timeout=0.50) # - Triggering the first podium.
    sleep(sleep_2) # - Awaiting next call.
    requests.get(op_2, timeout=0.50) # - Triggering the first podium.
    sleep(sleep_3) # - Awaiting turnoff.
    requests.get(op_3, timeout=0.50) # - Triggering the first podium.
    sleep(sleep_4) # - Awaiting end of Video(1).
    requests.get(op_4, timeout=0.50) # - Triggering the first podium.
    run('vcgencmd display_power 0', shell=True)
    kill_process = multiprocessing.Process(target=video_kill)
    kill_process.start()

#   Main Script
num = 1
while True:
    if num > 3:
        num = 1
    else:
        print(num)
        video_script(num)
        sleep(5)
        num = num + 1


# vlc --fullscreen --deinterlace-mode=auto video.mp4