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

SQL_ENYORA_TABLE=""" CREATE TABLE IF NOT EXISTS %s (
                    id integer PRIMARY KEY,
                    r_date text NOT NULL,
                    r_time text NOT NULL,
                    r_action text NOT NULL,
                    r_worked_time text,
                    r_day_off_work integer
                );"""

JSON_DIMENSION={'rowid': 0,
    'date': '01-01-1970',
    'time': '00:01:',
    'action': 'in',
    'worked_time': '',
    'day_off_work': 0
    }

'''SQL_LATEST_ROW=""" SELECT rowid,action,hour from %s 
                    WHERE r_date LIKE '%s' ORDER BY 
                    rowid DESC LIMIT 1; """'''

SQL_REQUEST_LAST_DAY=""" SELECT * FROM %s ORDER BY date(r_date) DESC Limit 20 """
SQL_LATEST_ROW=""" SELECT * FROM %s ORDER BY rowid DESC LIMIT 1; """
SQL_SELECT_ALL=""" SELECT * FROM %s ORDER BY rowid DESC; """

SQL_QUERY_IN=""" INSERT INTO %s 
				(r_date, r_time, r_action, r_worked_time, r_day_off_work) 
				VALUES ('%s','%s','%s', '%s', '%d')"""

