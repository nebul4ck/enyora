#!/usr/bin/python3


import argparse
import sys

parser = argparse.ArgumentParser(
	prog='enyora')
parser.add_argument(
	'-a',
	'--action',
	action='store',
	help='Use [in|out] to check on/from office. \
		Use [day|week|month] to show worked hours.')


if len(sys.argv)==1:
     parser.print_help(sys.stderr)
     sys.exit(1)

args = parser.parse_args()

print(args.action)