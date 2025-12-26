{\rtf1\ansi\ansicpg1252\cocoartf2867
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 # easy_button.py (replace play_sound)\
import subprocess, os\
\
SOUND = os.path.expanduser("~/that_was_easy.wav")  # use WAV for the aux jack\
\
def play_sound():\
    # -q quiet, -D default uses the selected output (headphones)\
    subprocess.run(["aplay", "-q", "-D", "default", SOUND], check=False)}