# -*- coding: utf8 -*-

"""
.. module:: settings
   :platform: Unix/Linux
   :synopsis: Initialize Config
.. moduleauthor::
   :Author: nebul4ck
   :mail: a.gonzalezmesas@gmail.com
   :Web : https://www.linkedin.com/in/nebul4ck/
   :Version : 0.0.1
"""

import configparser
import os,sys

# Parse config file
CONFIG_FILE = '/etc/enyora/enyora.conf'
DEV_CONFIG_FILE = './enyora.conf'

def Conf():

	config = configparser.ConfigParser()

	if os.path.isfile(CONFIG_FILE):
		print('INFO - Loading %s file' % CONFIG_FILE)
		config.read([CONFIG_FILE])
	elif os.path.isfile(DEV_CONFIG_FILE):
		print('INFO - Loading %s file' % DEV_CONFIG_FILE)
		config.read([DEV_CONFIG_FILE])
	else:
		print('ERROR - Config file not found.')
		sys.exit(1)

	return config