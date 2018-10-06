#!/usr/bin/python
# -*- coding: utf-8 -*-
# This Python file uses the following encoding: utf-8
import subprocess as sp
import os, sys

msg="""
Popen.returncode 
The child return code, set by poll() and wait() (and indirectly by communicate()). 
A None value indicates that the process hasn’t terminated yet.
A negative value -N indicates that the child was terminated by signal N (Unix only).
if you have not called poll or wait so returncode won't be set.

child = sp.Popen(openRTSP + opts.split(), stdout=sp.PIPE)
returnCode = child.poll()
or
child = sp.Popen(openRTSP + opts.split(), stdout=sp.PIPE)
data = child.communicate()[0]
err = child.communicate()[1]
rc = child.returncode
"""

def main():
   cmd="ls -al"
   child=sp.Popen(cmd, stdin=sp.PIPE, stdout=sp.PIPE,stderr=sp.PIPE, shell=True)
   data,err = child.communicate()
   rc = child.returncode
   print("data\n")
   for line in data.split("\n"):
       print(line)
   print ("\nreturncode="+str(rc))
   print("fixed codeing xe error, and data str print\n")

if __name__=="__main__":
    if "-a" in sys.argv[1:]:
        print ("-a")
    main()


