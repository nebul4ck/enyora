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

	def insert_row(self, database, table, cur_date, cur_time, 
					cur_action, worked):
		''' insert a row '''
		data_conn = self.open_connect(database)
		conn_db = data_conn['conn']
		cur = data_conn['cursor']

		if conn_db is not None:
			cur.execute(self.sql_query_in % (table, cur_date, cur_time, 
				cur_action, worked))
			conn_db.commit()
			conn_db.close()

	def request_row(self, database, table, statement):
		''' request row '''
		data_conn = self.open_connect(database)
		conn_db = data_conn['conn']
		cur = data_conn['cursor']

		if conn_db is not None:
			raw_request=cur.execute(statement % table).fetchall()
			conn_db.close()

		return raw_request