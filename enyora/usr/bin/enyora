#!/usr/bin/python3
# -*- coding: utf8 -*-

"""
.. module:: main
   :platform: Unix/Linux
   :synopsis: Binary prog
.. moduleauthor::
   :Author: nebul4ck
   :mail: a.gonzalezmesas@gmail.com
   :Web : https://www.linkedin.com/in/nebul4ck/
   :Version : 0.0.1
"""

import argparse
import sys
import traceback
import ast

from registry.lib.base import Base

def main():
	''' Main function. '''

	parser = argparse.ArgumentParser(
		prog='enyora',
		description='Enyora registry.',
		add_help=True)

	parser.add_argument(
		'-a',
		'--action',
		action='store',
		choices=['in',
			'out',
			'day',
			'week',
			'month'],
		help='in|out to record entry or exit time.\
			unit time to show about worked hours.')

	if len(sys.argv)==1:
	     parser.print_help(sys.stderr)
	     sys.exit(1)

	args = parser.parse_args()
	enyora_registry = Base()
	enyora_registry.run(args.action)

if __name__ == "__main__":
	main()

