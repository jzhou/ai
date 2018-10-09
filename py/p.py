#!/usr/bin/env python

import argparse
#https://www.daniweb.com/programming/software-development/threads/450614/how-do-i-pass-multiple-values-as-argument-when-using-arpgarse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-id', nargs = '*', dest = 'ids', required=False, help = 'some ids', default = argparse.SUPPRESS)
    #parser.add_argument('--id', nargs = '*', dest = 'ids', help = 'some ids', default = argparse.SUPPRESS)
    parser.add_argument('-a', action='store_true', required=False, help = 'some folders', default = argparse.SUPPRESS)
    #parser.add_argument('-p', nargs = '?', dest = 'folders', help = 'some folders', default = argparse.SUPPRESS)
    parser.add_argument('-ld', nargs = 1, dest = 'session', required=True,help = 'some folders', default = argparse.SUPPRESS)
    #With argparse.SUPPRESS, the option's dest will be removed from the namespace if it is 
    #missing from the command line.
    ns = parser.parse_args()
    print(ns)
    if "-id" in ns:
       print(ns.ids)
    #if ns.folders:
    #   print(ns.folders)
    if ns.session:
       print(ns.session)
    if ns.a:
       print("-a called")

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
