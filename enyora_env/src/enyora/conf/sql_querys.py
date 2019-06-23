# -*- coding: utf8 -*-

"""
.. module:: sql uerys
   :platform: Unix/Linux
   :synopsis: Set SQL querys
.. moduleauthor::
   :Author: nebul4ck
   :mail: a.gonzalezmesas@gmail.com
   :Web : https://www.linkedin.com/in/nebul4ck/
   :Version : 0.0.1
"""

''' SQLITE TIP: SQLite does not have a separate Boolean storage class. Instead, 
    Boolean values are stored as integers 0 (false) and 1 (true). '''

SQL_ENYORA_TABLE=""" CREATE TABLE IF NOT EXISTS %s (
                    id integer PRIMARY KEY,
                    r_date text NOT NULL,
                    r_time text NOT NULL,
                    r_action text NOT NULL,
                    r_worked_time text,
                    r_day_off_work integer
                );"""

SQL_DATE_SELECT=""" SELECT r_date,r_time FROM %s \
    ORDER BY date(r_date) DESC,time(r_time) DESC LIMIT 20; """

SQL_LAST_ACTION=""" SELECT r_action from %s WHERE r_date='%s'
    ORDER BY time(r_time) DESC LIMIT 1; """

SQL_QUERY_IN=""" INSERT INTO %s 
				(r_date, r_time, r_action, r_worked_time, r_day_off_work) 
				VALUES ('%s','%s','%s', '%s', '%d')"""

