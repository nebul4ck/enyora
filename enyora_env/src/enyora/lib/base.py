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
from enyora.conf.sql_querys import *
from enyora.lib.sql import sqlAction
from enyora.lib.actions import registryAction


class Base(object):
	"""Base class."""
	def __init__(self):
		self.name=self.__class__.__name__
		self.sql_latest_row=SQL_LATEST_ROW

		loadConf=baseConf()
		config=loadConf.Conf()

		self.enyora_db=ast.literal_eval(config['database']
			['enyora_db'])
		self.enyora_table=ast.literal_eval(config['database']
			['enyora_table'])

	def run(self, action):

		''' Initialize SQL Actions '''
		sql=sqlAction()

		check_sql_config=sql.check_config(self.enyora_db, 
			self.enyora_table)

		if not check_sql_config:
			print('Exiting with erros...')
			exit(1)

		''' Initialize Registry Actions '''
		registry_action=registryAction()

		''' Set current values '''
		date_time=registry_action.set_date_time()

		# Current values
		cur_date=date_time['date']
		cur_time=date_time['time']
		cur_action='in'

		# Default register values
		reg_date=''
		reg_time=''
		reg_action=''
		worked=''

		# Request the latest inserted row
		data_request=sql.request_row(self.enyora_db, self.enyora_table, 
			self.sql_latest_row)

		# Are registry date and current date the same?
		#	request: [(rowid, r_date, r_time, r_action, r_worked, r_incident, r_holidays)]
		try:
			reg_date=data_request[0][1]
			reg_time=data_request[0][2]
			reg_action=data_request[0][3]
		except IndexError:
			print('Recording the first reg into table...')
		except Exception as e:
			print(e)
			exit(1)

		if reg_date==cur_date:
			if reg_action==cur_action:
				cur_action='out'
				worked=registry_action.calc_work(reg_time, cur_time)

			print('Horas trabajadas: %s' % worked)

		# Insert values
		sql.insert_row(self.enyora_db, self.enyora_table, cur_date, 
			cur_time, cur_action, worked)