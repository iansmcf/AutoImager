#!/usr/bin/python3
from time import sleep
from picamera import PiCamera
# requires espeak,
#  pip3 install espeak
#  sudo apt-get install espeak
from gtts import gTTS
import os

camera = PiCamera()

#function for announcing purpose of next picture
def purpose_announce(string):
    tts = gTTS(text=string, lang='en')
    tts.save("work.mp3")
    os.system('omxplayer -o local work.mp3')

#function for taking a picture
def take_picture(resolution,preview_time,filename):
    # TODO: enable resolution setting, for now stick to 1080p
    # set resolution
    camera.resolution = (1920,1080)
    sleep(preview_time)
    camera.capture(filename)


purpose_announce("Start by facing me please")
purpose_announce("Taking picture")
take_picture("",10,'today-front.jpg')

purpose_announce("Okay, now turn left 90 degrees so that your right side is facing me.")
purpose_announce("Taking picture")
take_picture("",10,'today-right.jpg')

purpose_announce("Alright, now turn left 90 degrees so that you are facing away from me.")
purpose_announce("Taking picture")
take_picture("",10,'today-back.jpg')

purpose_announce("Okay, now just turn left one last time so that your left side is facing me.")
purpose_announce("Taking picture")
take_picture("",10,'today-left.jpg')

purpose_announce("Imaging complete. Have a nice day!")
