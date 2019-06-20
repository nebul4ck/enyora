# -*- coding: utf8 -*-

"""
.. module:: sql Actions
   :platform: Unix/Linux
   :synopsis: Config SQL actions
.. moduleauthor::
   :Author: nebul4ck
   :mail: a.gonzalezmesas@gmail.com
   :Web : https://www.linkedin.com/in/nebul4ck/
   :Version : 0.0.1
"""

import sqlite3
import os.path as path

from datetime import datetime, timedelta
from enyora.conf.sql_querys import *

class sqlAction(object):
	"""baseConf class"""
	def __init__(self):
		self.name=self.__class__.__name__
		self.sql_table=SQL_ENYORA_TABLE
		self.sql_latest_row=SQL_LATEST_ROW
		self.sql_query_in=SQL_QUERY_IN

	def open_connect(self, database):
		''' open a new connection.
			Return a connect and cursor objects '''

		try:
			conn_db = sqlite3.connect(database)
			cur = conn_db.cursor()

			data_conn = {
							'conn': conn_db,
							'cursor': cur
						}
		except Exception as e:
			print(e)

		return data_conn

	def create_database(self, database):
		'''ensure database exists '''

		db_exist=False

		if not path.isfile(database):
			try:
				data_conn=self.open_connect(database)
				conn_db=data_conn['conn']
				db_exist=True
			except Exception as e:
				print(e)
			finally:
				conn_db.close()

		return db_exist

	def create_table(self, database, table, sql_table):
		''' ensure table exists '''

		try:
			data_conn = self.open_connect(database)
			conn_db = data_conn['conn']
			cur = data_conn['cursor']
			make_table = sql_table % table
			cur.execute(make_table)
		except Error as e:
			print(e)
		finally:
			conn_db.close()

	def check_config(self, database, table):
		''' ensure database_registry and table exists '''

		
		stdout_check_config=True
		
		try:
			db_exist=self.create_database(database)
			if db_exist:
				self.create_table(database, table, self.sql_table)
		except Exception as e:
			print(e)
			stdout_check_config=False

		return stdout_check_config

	def check_day(self, database, table, date):
		''' return None, today, yesterday, past '''

		days=[]

		# Request
		data_request=self.request_row(database, table, 
			self.sql_latest_row)

		if not data_request:
			days.append(None)
		else:
			latest_row=data_request[0]
			req_day=latest_row[1]
			if req_day==date:
				days.append('today')
			elif req_day!=date:
				req_day_obj=datetime.strptime(req_day, '%Y-%m-%d')
				date_obj=datetime.strptime(date, '%Y-%m-%d')
				diferencia=date_obj - req_day_obj
				num_days=str(diferencia).split(' ')[0]

				day_sum = 0
				for day in range(1, int(num_days) + 1):
					day_sum += 1
					current_date=req_day_obj + timedelta(days=day_sum)
					days.append(str(current_date).split(' ')[0])

		return days

	def insert_record(self, database, table, date, time, 
					action, worked_time, day_off_work):
		''' Insert a new record '''

		''' Check if the latest action and current action
			are the same '''

		days=self.check_day(database, table, date)
		print(days)
		exit(0)

		# Is the first record in enyora_registry table
		if not days:
			''' Insert record '''
			print('[info] - Recording the first one register into office...')
			data_conn = self.open_connect(database)
			conn_db = data_conn['conn']
			cur = data_conn['cursor']

			print('Using \'clock-in\' for the first record by default.')
			if conn_db is not None:
				try:
					action='in'
					cur.execute(self.sql_query_in % (table, date, time, 
						action, worked_time, day_off_work))
					conn_db.commit()
					conn_db.close()
					print('[info] - Recorded new Clock-%s' % action)
					exit(0)
				except Exception as e:
					print(e)
					exit(1)
		else:
			YA TENGO LA LISTA DE DIAS Y PUEDE SER TODAY, YESTERDAY O UNA LISTA DE FECHAS
			SI ES UNA FECHA DE DIAS DETECTAR CUALES FUERON LOS 'FESTVOS' DEFINIR FESTIVOS EN CONF.
			UNA VEZ QUITADOS LOS FESTIVOS, ENVIAR A MENU LOS DIAS Y ACTUAR EN CONSECUENCIA
			# Set requested values
			# data_request=[(7, '2019-07-12', '12:02', 'out', '', 0)]
			latest_row=data_request[0]
			rec_date=latest_row[1]
			rec_time=latest_row[2]
			rec_action=latest_row[3]
			rec_worked_time=latest_row[4]
			rec_day_off_work=latest_row[5]


			exit(0)

	def request_row(self, database, table, statement):
		''' request row '''
		data_conn = self.open_connect(database)
		conn_db = data_conn['conn']
		cur = data_conn['cursor']

		if conn_db is not None:
			raw_request=cur.execute(statement % table).fetchall()
			conn_db.close()

		return raw_request