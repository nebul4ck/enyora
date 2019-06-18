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


class baseConf(object):
	"""baseConf class"""
	def __init__(self):
		self.name=self.__class__.__name__
		self.config_file='/etc/enyora/enyora.conf'
		self.dev_config_file='./enyora.conf-dev'

	def Conf(self):

		config = configparser.ConfigParser()

		if os.path.isfile(self.config_file):
			print('INFO - Loading %s file' % self.config_file)
			config.read([self.config_file])
		elif os.path.isfile(self.dev_config_file):
			print('INFO - Loading %s file' % self.dev_config_file)
			config.read([self.dev_config_file])
		else:
			print('ERROR - Config file not found.')
			sys.exit(1)

		return config