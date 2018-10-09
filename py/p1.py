#!/usr/bin/python 

import argparse

parser = argparse.ArgumentParser(prog='mydaemon')
sp = parser.add_subparsers()
sp_start = sp.add_parser('start', help='Starts %(prog)s daemon')
sp_stop = sp.add_parser('stop', help='Stops %(prog)s daemon')
sp_restart = sp.add_parser('restart', help='Restarts %(prog)s daemon')

parser.parse_args()
