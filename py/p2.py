#!/usr/bin/python 

import argparse
##ref: https://stackoverflow.com/questions/7869345/how-to-make-python-argparse-mutually-exclusive-group-arguments-without-prefix

parser = argparse.ArgumentParser(prog='mydaemon')
sp = parser.add_subparsers()
sp_start = sp.add_parser('-l', help='Starts %(prog)s daemon')
sp_stop = sp.add_parser('-s', nargs=1, help='Stops %(prog)s daemon')
sp_restart = sp.add_parser('-a', help='Restarts %(prog)s daemon')
sp_namet = sp.add_parser('name', help='Restarts %(prog)s daemon')


parser.parse_args()
