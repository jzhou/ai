import argparse

parser = argparse.ArgumentParser()

group = parser.add_mutually_exclusive_group(required=True)
group.add_argument('--foo', nargs=2,action='store_true')
group.add_argument('--bar', action='store_false')
group.add_argument('--zee', nargs=1,action='store_false')

settings = parser.parse_args()
