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
		self.name=self.__class__.__name__

		''' Loading config parameters '''
		loadConf=baseConf()
		config=loadConf.Conf()

		''' Set config parameters '''
		#self.sql_select_all=SQL_SELECT_ALL
		self.database=ast.literal_eval(config['database']
			['enyora_db'])
		self.table=ast.literal_eval(config['database']
			['enyora_table'])
		# self.reg_date=ast.literal_eval(config['default_values']
		# 	['reg_date'])
		# self.reg_time=ast.literal_eval(config['default_values']
		# 	['reg_time'])
		# self.default_action=ast.literal_eval(config['default_values']
		# 	['action'])
		# self.default_worked_time=ast.literal_eval(config['default_values']
		# 	['worked_time'])
		# self.default_day_off_work=ast.literal_eval(config['default_values']
		# 	['day_off_work'])

	def run(self, action):

		if action=='in' or action=='out':
			''' Insert new record '''

			# Initialize Registry Actions Class
			registry_action=registryAction()

			json_data=registry_action.clocking(self.database, self.table, action)

		elif action=='import':
			''' Import from Excel '''
			#TODO
		elif action=='export':
			'''Export to Excel '''
		else:
			''' Show worked hours '''
			#TODO:
				#DAY
				#WEEK
				#MONTH

		# # Initialize Events Class
		# incident=Events()


		# ''' Ensure database and table exists Stage '''
		# try:
		# 	check_sql_config=sql.check_config(self.enyora_db, 
		# 		self.enyora_table)
		# except Exception as e:
		# 	print('[error] - %s' % e)
		# 	print('[error] - Database and/or table could not be created')
		# 	print('... exiting with errors')
		# 	exit(1)				


		# ''' Check the latest record Stage '''

		# # Request
		# data_request=sql.request_row(self.enyora_db, self.enyora_table, 
		# 	self.sql_latest_row)

		# # Format JSON data
		# json_list=registry_action.format_data(data_request)


		# ''' Set current date/time Stage '''
		# date_time=registry_action.set_date_time()
		# cur_date=date_time['date']
		# cur_time=date_time['time']




		# # Is the same date?
		# if req_date==cur_date:
		# 	# then the action could not be the same
		# 	cur_action=registry_action.test_action(req_action)

		# 	#set_action=incident.another_rec()

		# print(latest_row)
		# exit(0)
		# #if 
		# try:
		# 	reg_date=json_data_req[0][1]
		# 	reg_time=data_request[0][2]
		# 	reg_action=data_request[0][3]
		# except IndexError:
		# 	no_worked=True
		# 	print('')
		# except Exception as e:
		# 	print(e)
		# 	exit(1)

		# if reg_date==cur_date:
		# 	if reg_action==cur_action:
		# 		cur_action='out'
		# 		worked_time=registry_action.calc_work(reg_time, cur_time)

		# 	print('Horas trabajadas: %s' % worked)

