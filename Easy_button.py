#!/usr/bin/env python3
from gpiozero import Button
from signal import pause
import subprocess
import time
import os

BUTTON_GPIO = 17                   # physical pin 11
SOUND_FILE = "/home/pi/Desktop/that_was_easy.wav"  # put your audio here
DEBOUNCE_S = 0.30
_last = 0.0

btn = Button(BUTTON_GPIO, pull_up=True, bounce_time=0.05)

def play_sound():
    # WAV via aplay is fast and reliable (works with Bluetooth sink if it's default output)
    subprocess.run(["aplay", "-q", SOUND_FILE], check=False)

def on_press():
    global _last
    now = time.time()
    if now - _last < DEBOUNCE_S:
        return
    _last = now
    play_sound()

btn.when_pressed = on_press
print("Easy button running. Press the button!")
pause()
