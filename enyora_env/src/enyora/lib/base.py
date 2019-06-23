# -*- coding: utf8 -*-

"""
.. module:: base
   :platform: Unix/Linux
   :synopsis: Initialize Enyora
.. moduleauthor::
   :Author: nebul4ck
   :mail: a.gonzalezmesas@gmail.com
   :Web : https://www.linkedin.com/in/nebul4ck/
   :Version : 0.0.1
"""


import ast

from enyora.conf.settings import baseConf
from enyora.lib.actions import registryAction

class Base(object):
	"""Base class."""
	def __init__(self):
		super(Base, self).__init__()
		#self.name=self.__class__.__name__

		''' Loading config parameters '''
		loadConf=baseConf()
		self.config=loadConf.Conf()

		''' Loading Enyora Registry Actions '''
		self.registry_action=registryAction(self.config)

	def run(self, action):

		''' Ensure database and table exists '''
		self.registry_action.check_config()

		if action=='in' or action=='out':
			''' Insert new record '''
			json_data=self.registry_action.clocking(action)
		else:
			print('Action not found!')
			exit(1)

