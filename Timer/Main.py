import sys
import time
from playsound import playsound
from threading import Thread


def our_timer(seconds):

    thread = Thread(target=playsound,args=("./Timer/beep_sound.mp3",), daemon=True)
    for i in range(seconds-1, -1, -1):
        sys.stdout.write("\r Timer : %s" %i)
        if i == 9:
            thread.start()
        time.sleep(1)
        sys.stdout.flush()



if __name__ == "__main__":
    seconds = int(sys.argv[1])
    our_timer(seconds)