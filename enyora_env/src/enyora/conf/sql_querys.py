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
                    r_action text NOT NULL,
                    r_worked text
                );"""

SQL_DATE_SELECT=""" SELECT r_date FROM %s \
    ORDER BY datetime(r_date) DESC LIMIT 1; """

SQL_LAST_ACTION=""" SELECT r_action from %s WHERE r_date='%s'
    ORDER BY date(r_date) DESC LIMIT 1; """

SQL_QUERY_IN=""" INSERT INTO %s
    (r_date, r_action, r_worked) VALUES ('%s','%s','%s')"""

SQL_WORKED=""" SELECT r_worked from {} WHERE
        (r_date BETWEEN strftime('%Y-%m-%d', '{}') AND
        datetime('now', 'localtime')) AND
        (r_worked IS NOT ''); """


#SQL_LAST_DAY_MONTH=""" SELECT date(
#    'now','start of month','+1 month','-1 day'); """
#SQL_FIRST_DAY_OF_WEEK=""" SELECT date('now', 'weekday 0', '-6 days'); """


# Otra forma con python de sacar el primer dia de la semana
# day = '2019-06-25'
# dt = datetime.strptime(day, '%Y-%m-%d')
# start = dt - timedelta(days=dt.weekday())



