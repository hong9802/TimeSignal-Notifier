import subprocess
import time
from datetime import datetime

def play_mp3(TimeSignalpath):
    subprocess.Popen(['mpg123', '-q', TimeSignalpath]).wait()

while(True):
    TimeSignalpath = "TimeSignal/" + str(datetime.now().hour) + ".mp3"
    if(datetime.now().minute == 0 and datetime.now().second == 0):
        play_mp3(TimeSignalpath)
    else:
        time.sleep(1)
        pass