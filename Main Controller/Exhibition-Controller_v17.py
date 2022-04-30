# Version | 14.00
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


X = 0

#   Video Location
video = Path("Desktop/video.mp4")
media = vlc.MediaPlayer("video.mp4")

#   Inital Start-Up. Turning Off All.
#       Lighting
requests.get(P1_OFF, timeout=0.50)
sleep(0.5)
requests.get(P2_OFF, timeout=0.50)
sleep(0.5)
requests.get(P3_OFF, timeout=0.50)
sleep(0.5)
#       Features
requests.get(P1_X_OFF, timeout=0.50)
sleep(0.5)
requests.get(P2_X_OFF, timeout=0.50)
sleep(0.5)
requests.get(P3_X_OFF, timeout=0.50)
sleep(0.5)

def video_play_1():
    subprocess.run('vlc --fullscreen --deinterlace-mode=auto 1_01-XHive.mp4', shell=True)

def video_play_2():
    subprocess.run('vlc --fullscreen --deinterlace-mode=auto video.mp4', shell=True)

def video_play_3():
    subprocess.run('vlc --fullscreen --deinterlace-mode=auto 1_01-XHive.mp4', shell=True)

def video_kill():
    subprocess.run('killall -9 vlc', shell=True)

#num = 1 # - Default Video as Number 1
#video_number = (f'video_play_{num}')
#print(video_number)

def video_process_1():
    video_process = multiprocessing.Process(target=video_play_1)
    video_process.start()
    sleep(1) # - Allowing video to render.
    requests.get(P1_ON, timeout=0.50) # - Triggering the first podium.
    sleep(90) # - Awaiting next call.
    requests.get(P1_X_ON, timeout=0.50) # - Triggering the first podium.
    sleep(30) # - Awaiting turnoff.
    requests.get(P1_X_OFF, timeout=0.50) # - Triggering the first podium.
    sleep(89) # - Awaiting end of Video(1).
    requests.get(P1_OFF, timeout=0.50) # - Triggering the first podium.
    kill_process = multiprocessing.Process(target=video_kill)
    kill_process.start()

def video_process_test():
    video_process = multiprocessing.Process(target=video_play_1)
    video_process.start()
    sleep(1) # - Allowing video to render.
    requests.get(P1_ON, timeout=0.50) # - Triggering the first podium.
    sleep(3) # - Awaiting next call.
    requests.get(P1_X_ON, timeout=0.50) # - Triggering the first podium.
    sleep(3) # - Awaiting turnoff.
    requests.get(P1_X_OFF, timeout=0.50) # - Triggering the first podium.
    sleep(3) # - Awaiting end of Video(1).
    requests.get(P1_OFF, timeout=0.50) # - Triggering the first podium.
    kill_process = multiprocessing.Process(target=video_kill)
    kill_process.start()

def video_script(num): 
    if num == 1:
        print("1")
        video_process = multiprocessing.Process(target=video_play_1)
        video_process.start()
        sleep_1 = 1
        sleep_2 = 1
        sleep_3 = 1
        sleep_4 = 1
        op_1 = 'http://192.168.4.1/P1_ON?'
        op_2 = 'http://192.168.4.1/P1_X_ON?'
        op_3 = 'http://192.168.4.1/P1_X_OFF?'
        op_4 = 'http://192.168.4.1/P1_OFF?'

    elif num == 2:
        print("2")
        video_process = multiprocessing.Process(target=video_play_2)
        video_process.start()
        sleep_1 = 2
        sleep_2 = 1
        sleep_3 = 2
        sleep_4 = 1
        op_1 = 'http://192.168.4.1/P2_ON?'
        op_2 = 'http://192.168.4.1/P2_X_ON?'
        op_3 = 'http://192.168.4.1/P2_X_OFF?'
        op_4 = 'http://192.168.4.1/P2_OFF?'

    elif num == 3:
        print("3")
        video_process = multiprocessing.Process(target=video_play_3)
        video_process.start()
        sleep_1 = 4
        sleep_2 = 4
        sleep_3 = 1
        sleep_4 = 1
        op_1 = 'http://192.168.4.1/P3_ON?'
        op_2 = 'http://192.168.4.1/P3_X_ON?'
        op_3 = 'http://192.168.4.1/P3_X_OFF?'
        op_4 = 'http://192.168.4.1/P3_OFF?'

    else:
        print("You've Fucked it somewhere along the way my friend. sorry.")
    
    print(op_1, op_2, op_3, op_4)
    sleep(sleep_1) # - Allowing video to render.
    requests.get(op_1, timeout=0.50) # - Triggering the first podium.
    sleep(sleep_2) # - Awaiting next call.
    requests.get(op_2, timeout=0.50) # - Triggering the first podium.
    sleep(sleep_3) # - Awaiting turnoff.
    requests.get(op_3, timeout=0.50) # - Triggering the first podium.
    sleep(sleep_4) # - Awaiting end of Video(1).
    requests.get(op_4, timeout=0.50) # - Triggering the first podium.
    kill_process = multiprocessing.Process(target=video_kill)
    kill_process.start()

#   Main Script
while True:
    #video_process_1()
    video_script(2)
#    video_process.start()
#    sleep(1) # - Allowing video to render.
#    requests.get(P1_ON, timeout=0.50) # - Triggering the first podium.
#    sleep(90) # - Awaiting next call.
#    requests.get(P1_X_ON, timeout=0.50) # - Triggering the first podium.
#    sleep(30) # - Awaiting turnoff.
#    requests.get(P1_X_OFF, timeout=0.50) # - Triggering the first podium.
#    sleep(89) # - Awaiting end of Video(1).
#    requests.get(P1_OFF, timeout=0.50) # - Triggering the first podium.
    sleep(5) # - Awaiting Start of video(2)
    requests.get(P2_ON, timeout=0.50) # - Triggering the first podium.
    sleep(5) # - Awaiting next call.
    requests.get(P2_X_ON, timeout=0.50) # - Triggering the first podium.
    sleep(5) # - Awaiting turnoff.
    requests.get(P2_X_OFF, timeout=0.50) # - Triggering the first podium.
    sleep(5) # - Awaiting end of Video(2.
    requests.get(P2_OFF, timeout=0.50) # - Triggering the first podium.
    sleep(5) # - Awaiting Start of video(3)
    requests.get(P3_ON, timeout=0.50) # - Triggering the first podium.
    sleep(5) # - Awaiting next call.
    requests.get(P3_X_ON, timeout=0.50) # - Triggering the first podium.
    sleep(5) # - Awaiting turnoff.
    requests.get(P3_X_OFF, timeout=0.50) # - Triggering the first podium.
    sleep(5) # - Awaiting end of Video(3).
    requests.get(P3_OFF, timeout=0.50) # - Triggering the first podium.
    sleep(5) # - Awaiting Start of video(1)
    #player.quit()
    video_process.close()

# vlc --fullscreen --deinterlace-mode=auto video.mp4