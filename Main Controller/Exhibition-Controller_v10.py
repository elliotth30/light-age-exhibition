# Version | 8.00
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
video = Path("/video.mp4")

#   Inital Start-Up. Turning Off All.
#       Lighting
requests.get(P1_OFF, timeout=0.50)
sleep(500)
requests.get(P2_OFF, timeout=0.50)
sleep(500)
requests.get(P3_OFF, timeout=0.50)
sleep(500)
#       Features
requests.get(P1_X_OFF, timeout=0.50)
sleep(500)
requests.get(P2_X_OFF, timeout=0.50)
sleep(500)
requests.get(P3_X_OFF, timeout=0.50)
sleep(500)

#   Main Script
while True:
    player = OMXPlayer(video) # - Starting Video
    sleep(5) # - Allowing video to render.
    requests.get(P1_ON, timeout=0.50) # - Triggering the first podium.
    sleep(5) # - Awaiting next call.
    requests.get(P1_X_ON, timeout=0.50) # - Triggering the first podium.
    sleep(5) # - Awaiting turnoff.
    requests.get(P1_X_OFF, timeout=0.50) # - Triggering the first podium.
    sleep(5) # - Awaiting end of Video(1).
    requests.get(P1_OFF, timeout=0.50) # - Triggering the first podium.
    sleep(5) # - Awaiting Start of video(2)
    requests.get(P1_ON, timeout=0.50) # - Triggering the first podium.
    sleep(5) # - Awaiting next call.
    requests.get(P1_X_ON, timeout=0.50) # - Triggering the first podium.
    sleep(5) # - Awaiting turnoff.
    requests.get(P1_X_OFF, timeout=0.50) # - Triggering the first podium.
    sleep(5) # - Awaiting end of Video(2.
    requests.get(P1_OFF, timeout=0.50) # - Triggering the first podium.
    sleep(5) # - Awaiting Start of video(3)
    requests.get(P1_ON, timeout=0.50) # - Triggering the first podium.
    sleep(5) # - Awaiting next call.
    requests.get(P1_X_ON, timeout=0.50) # - Triggering the first podium.
    sleep(5) # - Awaiting turnoff.
    requests.get(P1_X_OFF, timeout=0.50) # - Triggering the first podium.
    sleep(5) # - Awaiting end of Video(3).
    requests.get(P1_OFF, timeout=0.50) # - Triggering the first podium.
    sleep(5) # - Awaiting Start of video(1)
    player.quit()