# -*- coding: utf8 -*-

"""
.. module:: Actions
   :platform: Unix/Linux
   :synopsis: Initialize Actions
.. moduleauthor::
   :Author: nebul4ck
   :mail: a.gonzalezmesas@gmail.com
   :Web : https://www.linkedin.com/in/nebul4ck/
   :Version : 0.0.1
"""

import ast

from datetime import datetime, timedelta
from enyora.lib.sql import sqlAction
from enyora.conf.sql_querys import *
from enyora.conf.cod_messages import cod_20, cod_21, \
    cod_22, cod_23, cod_24

class registryAction(object):
    """Registry class"""
    def __init__(self, config):
        self.name=self.__class__.__name__

        self.config=config
        self.database=ast.literal_eval(config['database']
            ['enyora_db'])
        self.table=ast.literal_eval(config['database']
            ['enyora_table'])
        self.sql=sqlAction(self.config)

        self.sql_date_select=SQL_DATE_SELECT
        self.select_last_action=SQL_LAST_ACTION
        self.sql_worked=SQL_WORKED

    def check_config(self):
        ''' Database orchestration '''
        self.sql.database_orch()

    def set_date(self):
        ''' Set current date '''
        
        date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        return date

    def calc_work(self, last_date, curr_date, action):
        ''' set diff time '''

        date_for='%Y-%m-%d %H:%M:%S'
        worked=''

        if action=='out':
            parse_last_date=datetime.strptime(last_date, date_for)
            parse_curr_date=datetime.strptime(curr_date, date_for)
            worked=parse_curr_date - parse_last_date
            
        return worked

    def show_menu(self, last_date, last_action):
        ''' Launch the menu to force data insertion '''

        if last_action=='in':
            req_action='out'
        else:
            req_action='in'

        date_for='%Y-%m-%d %H:%M:%S'
        parse_date=datetime.strptime(last_date, date_for)
        opt_date=parse_date + timedelta(hours=2)
        parse_opt_date=datetime.strftime(opt_date, date_for)

        print('\n # Fix broken entry point #')
        print(' Latest entry-point recorded:\n')
        print('  | Date: %s' % last_date)
        print('  | Action: clock-%s' % last_action)
        print('\n The clock-%s action is required for day %s' % 
            (req_action, last_date))
        new_date=str(input('\n  Date [%s]: ' % opt_date))
        new_action=str(input('  Action [%s]: ' % req_action))

        # TODO: Check if the entering values are format correct.
        if new_date=='':
            new_date=parse_opt_date

        if new_action=='':
            new_action=req_action

        now=datetime.now()
        stderr_date=self.check_date(new_date, last_date, now)

        if not stderr_date:
            worked=self.calc_work(last_date, new_date, new_action)
            self.sql.insert_record(new_date, new_action, worked)
        else:
            print(stderr_date)
            exit(1)

    def last_day_recorded(self):
        ''' Return the last day recorded in enyora registry table '''

        statement=self.sql_date_select % self.table

        # Si no hay nada devuelve: []
        # Si si hay devuelve esto: [('2019-06-24 21:41:03',)]
        last_date=self.sql.request_row(statement)
        if not last_date:
            last_date=None
        else:
            last_date=last_date[0][0]

        return last_date

    def check_date(self, new_date, last_date, now):
        ''' Return if current datetime is valid '''

        stderr=None

        date_for='%Y-%m-%d %H:%M:%S'

        parse_new_date=datetime.strptime(new_date, date_for)
        parse_last_date=datetime.strptime(last_date, date_for)

        if parse_new_date > now:
            stderr=cod_20
        elif parse_new_date < parse_last_date:
            stderr=cod_21 % (last_date)

        return stderr

    def check_action(self, date, action):
        ''' Return if the current action and last action
            are the same '''
        
        statement=self.select_last_action % (self.table, date)
        try:
            last_action=self.sql.request_row(statement)[0][0]
        except IndexError:
            last_action=None
        else:
            if action==last_action:
                print(cod_22 % (action, last_action))
                print(cod_23)
                print(cod_24)
                self.show_menu(date, last_action)

        return action

    def show_worked_hours(self, from_ago):
        ''' Request worked hours for from_ago '''

        list_sum=[]

        day='%d'
        month='%m'
        year='%Y'

        day=datetime.now().strftime(day)
        month=datetime.now().strftime(month)
        year=datetime.now().strftime(year)

        today='%s-%s-%s' % (year, month, day)

        if from_ago=='today':
            date=today
        elif from_ago=='week':
            dt = datetime.strptime(today, '%Y-%m-%d')
            date=dt - timedelta(days=dt.weekday())
        elif from_ago=='month':
            date='%s-%s-01' % (year, month)
            print(date)
        elif from_ago=='year':
            date="%s-01-01" % (year)

        statement=self.sql_worked.format(self.table, date)
        worked=self.sql.request_row(statement)

        # Make another func passing worked list
        for time in worked:
            list_sum.append(time[0])

        totalSecs=0
        for tm in list_sum:
            timeParts=[int(s) for s in tm.split(':')]
            totalSecs+=(timeParts[0] * 60 + timeParts[1]) * 60 + timeParts[2]
        
        totalSecs, sec = divmod(totalSecs, 60)
        hr, min = divmod(totalSecs, 60)
        show_worked='%d:%02d:%02d' % (hr, min, sec)
        
        return show_worked

    def clocking(self, action):

            ''' Set current datetime '''
            curr_date=self.set_date()

            last_date=self.last_day_recorded()

            if not last_date:
                worked=''
                self.sql.insert_record(curr_date, action, worked)
                exit(0)

            action=self.check_action(last_date, action)
            worked=self.calc_work(last_date, curr_date, action)
            self.sql.insert_record(curr_date, action, worked)
            exit(0)