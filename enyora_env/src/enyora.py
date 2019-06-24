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

from enyora.lib.base import Base
from enyora.conf.cod_messages import cod_01


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
			'out'],
		required=True,
		dest='action',
		help=cod_01)

	if len(sys.argv)==1:
	     parser.print_help(sys.stderr)
	     sys.exit(1)

	args = parser.parse_args()
	enyora_registry = Base()
	enyora_registry.run(args.action)

if __name__ == "__main__":
	main()

