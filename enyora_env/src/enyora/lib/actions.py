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

    def check_config(self):
        ''' Database orchestration '''
        self.sql.database_orch()

    def set_date_time(self):
        ''' Set current date '''

        date_time={}
        
        date = datetime.today().strftime('%Y-%m-%d')
        time = datetime.now().strftime('%H:%M:%S')

        date_time={'date': date,'time': time}

        return date_time

    def calc_work(self, last_action, start_time, 
        finish_time):
        ''' set diff time '''

        time_format="%H:%M:%S"
        diff=''

        if last_action=='in':
            parse_start_hour=datetime.strptime(start_time, time_format)
            parse_finish_hour=datetime.strptime(finish_time, time_format)

            diff=parse_finish_hour - parse_start_hour

        return diff

    def show_menu(self, last_day, last_time, last_action):
        ''' Launch the menu to force data insertion '''

        if last_action=='in':
            req_action='out'
        else:
            req_action='in'

        time_format="%H:%M:%S"
        parse_time=datetime.strptime(last_time, time_format)
        opt_time=parse_time + timedelta(hours=2)
        parse_opt_time=datetime.strftime(opt_time, time_format)

        print('\n # Fix broken entry point #')
        print(' Latest entry-point recorded:\n')
        print('  | Date: %s' % last_day)
        print('  | Time: %s' % last_time)
        print('  | Action: clock-%s' % last_action)
        print('\n The clock-%s action is required for day %s' % 
            (req_action, last_day))
        new_day=str(input('\n  Date [%s]: ' % last_day))
        new_time=str(input('  Time [%s]: ' % parse_opt_time))
        new_action=str(input('  Action [%s]: ' % req_action))

        # TODO: Check if the entering values are format correct.
        if new_day=='':
            new_day=last_day

        if new_time=='':
            new_time=parse_opt_time

        if new_action=='':
            new_action=req_action

        date_is_valid=self.check_datetime(new_day, new_time)

        if date_is_valid:

            worked_time=self.calc_work(last_action, last_time, 
                new_time)

            self.sql.insert_record(new_day, new_time, new_action, 
                worked_time, day_off_work=0)

    def last_day_recorded(self):
        ''' Return the last day recorded in enyora registry table '''

        last_info={'date': None, 'time': None}

        statement=self.sql_date_select % self.table
        data_request=self.sql.request_row(statement)

        if data_request:
            latest_row=data_request[0]
            last_day=latest_row[0]
            last_time=latest_row[1]

            last_info={'date': last_day,
                'time': last_time}

        return last_info

    def check_datetime(self, date, time):
        ''' Return if current datetime is valid '''

        date_time_format='%Y-%m-%d %H:%M:%S'
        date_time='%s %s' % (date, time)

        parse_datetime=datetime.strptime(date_time, 
            date_time_format)

        if parse_datetime > datetime.now():
            print('Current time cannot to be future.')
            exit(1)
        else:
            is_valid=True

        return is_valid

    def check_action(self, day, action):
        ''' Return if the current action and last action
            are the same '''

        actions={'curr_action': action,
            'last_action': None,
            'are_same': False}
        
        statement=self.select_last_action % (self.table, day)
        last_action=self.sql.request_row(statement)[0][0]

        actions['last_action']=last_action

        if actions['curr_action']==last_action:
            actions['are_same']=True

        return actions

    def clocking(self, action):

            ''' Set current datetime '''
            date_time=self.set_date_time()
            current_date=date_time['date']
            current_time=date_time['time']

            last_date_info=self.last_day_recorded()
            last_day=last_date_info['date']
            last_time=last_date_info['time']
            


            date_is_valid=self.check_datetime(current_date, current_time)

            if date_is_valid:

                if not last_day:

                    worked_time=''

                    print('[info] - Recording the first one entry point to office...')
                    self.sql.insert_record(current_date, current_time, action, 
                        worked_time, 0, initialize=True)

                actions=self.check_action(last_day, action)
                last_action=actions['last_action']

                if actions['are_same']:
                    print('[warning] - the current action Clock-(%s) and the last action Clock-(%s) cannot the same.' % 
                        (action, last_action))
                    print('[info] - please, fix the problem:')
                    print('Launching MENU...')
                    self.show_menu(last_day, last_time, last_action)

                # If actions are not the same, and current action 
                #is out, calc time worked
                worked_time=self.calc_work(last_action, last_time, 
                    current_time)

                self.sql.insert_record(current_date, current_time, action, 
                    worked_time, day_off_work=0)
                exit(0)
