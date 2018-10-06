#!/usr/bin/python
# -*- coding: utf-8 -*-

import signal, os
import time

def handler(signum, frame):
    print ("Signal handler called with signal: " +str(signum))
    print ("complete operations needed when alarm received")

def main():

    signal.signal(signal.SIGALRM, handler)
    print ("set alarm signal")
    signal.alarm(3)
    print ("before alarm")
    time.sleep(5)
    signal.alarm(0)          # Disable the alarm
    print ("after alarm,  alarm disabled")
   
if __name__=="__main__":
    main()
