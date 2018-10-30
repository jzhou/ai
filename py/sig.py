#!/usr/bin/python

import signal, os
import time

def handler(signum, frame):
    print 'Signal handler called with signal', signum
    #raise IOError("Couldn't open device!")
    print ("handler called")

def main():
    # Set the signal handler and a 5-second alarm
    signal.signal(signal.SIGALRM, handler)
    signal.alarm(5)
    print("signal alarm started")

    # This open() may hang indefinitely
    #fd = os.open('/dev/ttyS0', os.O_RDWR)
    print("do something, then sleep")
    time.sleep(10) 
    print("do something")

    signal.alarm(0)          # Disable the alarm
    print("signal disabled")


if __name__=="__main__":
    main()
