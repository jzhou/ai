#!/usr/bin/env python

import argparse
import os,sys
#https://www.daniweb.com/programming/software-development/threads/450614/how-do-i-pass-multiple-values-as-argument-when-using-arpgarse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("ltTest", type=str, help="display letTest")
    parser.add_argument('-l', "--level", nargs = '+', dest = 'level', 
                        required=False, help = 'some ids', default = argparse.SUPPRESS)
    #parser.add_argument('-l', "--level", nargs = '+', dest = 'sls', required=False, help = 'some ids', default = argparse.SUPPRESS)
    #parser.add_argument('--id', nargs = '*', dest = 'ids', help = 'some ids', default = argparse.SUPPRESS)
    parser.add_argument('-a',"--all",  action='store_true', required=False, help = 'some folders', default = argparse.SUPPRESS)
    #parser.add_argument('-p', nargs = '?', dest = 'folders', help = 'some folders', default = argparse.SUPPRESS)
    parser.add_argument('-s',"--session", nargs = 1, dest = 'session', required=False,help = 'some folders', default = argparse.SUPPRESS)
    #parser.add_argument('-ld', nargs = 1, dest = 'session', required=True,help = 'some folders', default = argparse.SUPPRESS)
    #With argparse.SUPPRESS, the option's dest will be removed from the namespace if it is 
    #missing from the command line.
    if len(sys.argv[1:]) !=0:
        ns = parser.parse_args()
        print(ns)
        if ns.session and (ns.all or ns.level):
            print ("-a, -s|-l are mutually exclusive ...")
            sys.exit(2)
        if "-sl" in ns:
            print(ns.sls)
        elif "-ld" in ns:
            print(ns.session)
        elif "-a" in ns:
            print("-a called")
    else:
        print ("no parsing needed")

"""
Emily:py Emily$ ./p.py -h
usage: p.py [-h] [--id [IDS [IDS ...]]] [-p [FOLDERS [FOLDERS ...]]]

optional arguments:
  -h, --help            show this help message and exit
  --id [IDS [IDS ...]]  some ids
  -p [FOLDERS [FOLDERS ...]]
                        some folders
Emily:py Emily$ ./p.py --id 12345 65432 -p test1 test2 test3
Namespace(folders=['test1', 'test2', 'test3'], ids=['12345', '65432'])
Emily:py Emily$ vi p.py
Emily:py Emily$ ./p.py --ids 12345 6789 -p test test3
usage: p.py [-h] [--id [IDS [IDS ...]]] [-p [FOLDERS [FOLDERS ...]]]
p.py: error: unrecognized arguments: --ids 12345 6789
Emily:py Emily$ ./p.py --id 12345 65432 -p test1 test2 test3
Namespace(folders=['test1', 'test2', 'test3'], ids=['12345', '65432'])
['12345', '65432']
['test1', 'test2', 'test3']
Emily:py Emily$ 
"""
