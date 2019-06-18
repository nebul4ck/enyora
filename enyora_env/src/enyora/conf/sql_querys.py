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
                    r_hour text NOT NULL,
                    r_action text NOT NULL,
                    r_worked text
                );"""

'''SQL_LATEST_ROW=""" SELECT rowid,action,hour from %s 
                    WHERE r_date LIKE '%s' ORDER BY 
                    rowid DESC LIMIT 1; """'''

SQL_LATEST_ROW=""" SELECT * from %s ORDER BY rowid DESC LIMIT 1; """

SQL_QUERY_IN=""" INSERT INTO %s 
				(r_date, r_hour, r_action, r_worked) 
				VALUES ('%s','%s','%s', '%s')"""