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
import ast
import os.path as path

from datetime import datetime, timedelta
from enyora.conf.sql_querys import *
from enyora.conf.cod_messages import cod_30, cod_31, \
	cod_32

class sqlAction(object):
	"""baseConf class"""
	def __init__(self, config):
		self.name=self.__class__.__name__

		self.config=config
		self.database=ast.literal_eval(config['database']
			['enyora_db'])
		self.table=ast.literal_eval(config['database']
			['enyora_table'])

		self.sql_table=SQL_ENYORA_TABLE
		self.sql_query_in=SQL_QUERY_IN

	def open_connect(self):
		''' open a new connection.
			Return a connect and cursor objects '''
		try:
			conn_db = sqlite3.connect(self.database)
			cur = conn_db.cursor()

			data_conn = {'conn': conn_db, 
				'cursor': cur}
		except Exception as e:
			print(e)

		return data_conn

	def create_database(self):
		'''ensure database exists '''

		db_exist=True

		if not path.isfile(self.database):
			try:
				data_conn=self.open_connect()
				conn_db=data_conn['conn']
				db_exist=True
				print(cod_30 % self.database)
			except Exception as e:
				print(e)
				db_exist=False
			finally:
				conn_db.close()

		return db_exist

	def create_table(self):
		''' ensure table exists '''

		try:
			data_conn=self.open_connect()
			conn_db=data_conn['conn']
			cur=data_conn['cursor']
			make_table=self.sql_table % self.table
			cur.execute(make_table)
		except Error as e:
			print(e)
		finally:
			conn_db.close()

	def database_orch(self):
		''' ensure database_registry and table exists '''
		
		stdout_check_config=True

		try:
			db_exist=self.create_database()
			if db_exist:
				self.create_table()
		except Exception as e:
			print(e)
			stdout_check_config=False

	def request_row(self, statement):
		''' request row '''
		data_conn=self.open_connect()
		conn_db=data_conn['conn']
		cur = data_conn['cursor']

		if conn_db is not None:
			raw_request=cur.execute(statement).fetchall()
			conn_db.close()

		return raw_request

	def insert_record(self, date, action, worked):
		'''Insert a new record into database '''

		data_conn = self.open_connect()
		conn_db = data_conn['conn']
		cur = data_conn['cursor']

		statement=self.sql_query_in % (self.table, date, 
			action, worked)

		if conn_db is not None:
			try:
				cur.execute(statement)
				print(cod_31 % action)
				conn_db.commit()
				conn_db.close()
			except Exception as e:
				print(e)
				exit(1)
		else:
			print(cod_32)
			exit(1)
