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

import json

from datetime import datetime
from enyora.lib.sql import sqlAction
from enyora.conf.sql_querys import *

class registryAction(object):
    """Registry class"""
    def __init__(self):
        self.name=self.__class__.__name__
        self.select_latest_row=SQL_LATEST_ROW
        self.json_dim=JSON_DIMENSION

    def set_date_time(self):
        ''' Set current date '''

        date_time = {}
        
        date = datetime.today().strftime('%Y-%m-%d')
        time = datetime.now().strftime('%H:%M')

        date_time = { 'date': date, 'time': time }

        return date_time

    def calc_work(self, start_time, finish_time):
        ''' set diff time '''

        time_format = "%H:%M"

        parse_start_hour = datetime.strptime(start_time, time_format)
        parse_finish_hour = datetime.strptime(finish_time, time_format)

        diff = parse_finish_hour - parse_start_hour

        return diff

    def format_data(self, data):
        ''' from tuple to json '''


        self.json_dim['rowid']=data[0]
        self.json_dim['date']=data[1]
        self.json_dim['time']=data[2]
        self.json_dim['action']=data[3]
        self.json_dim['worked_time']=data[4]
        self.json_dim['day_off_work']=data[5]

        return self.json_dim

    def test_action(self, req_date, req_action):
        ''' ensure the latest recorded action and the current
            action are not the same '''

        recorded_action=req_action

        if recorded_action=='in':
            current_action='out'
        else:
            current_action='in'

        set_answer=str(input('\nThe latest recorded action is %s. The\
            current action must be %s. Is it true? (y/n)' & (recorded_action, 
                current_action)))

        if set_answer=='n':
            print('There was an incident, you must mark the last check')
            old_mark=str(input('\nSet the time for the last check %s (%s). ie. 18:00'))

        stderr = False

        try:
            data_conn = open_connect(db_file)
            conn_db = data_conn['conn']
            cur = data_conn['cursor']

            req = req_last_row % (table_name, date)
            last_row = cur.execute(req)
            raw_row = last_row.fetchone()
            last_action = raw_row[1]


            if last_action == action:
                stderr = True

        except TypeError as e:
            print('Welcome!, gl&hf :D')
            stderr = None
        except Exception as e:
            print(e)
            raise
        finally:
            conn_db.close()

        return stderr

    def clocking(self, database, table, action):

            ''' Set current datetime '''
            date_time=self.set_date_time()
            current_date=date_time['date']
            current_time=date_time['time']

            sql=sqlAction()
            # Insert values
            sql.insert_record(database, table, current_date, current_time,
                action, '', 0)

            # Adding a new record

            # Get the latest record in JSON format
            latest_day_record=data_request[0]
            latest_record_json=self.format_data(latest_day_record)
            # requested values
            latest_date=latest_record_json['date']
            latest_time=latest_record_json['time']
            latest_action=latest_record_json['action']
            return latest_record_json

    # def get_rows(self):

    #     file = open('./dates.db','r')
    #     lines = file.readlines()

    #     entrance = lines[0].split('|')[1]
    #     leave = lines[-1].split('|')[1]

    #     times = {'start': entrance, 'leave': leave}

    #     return times

    # def insert_file_row(self, date, time):
    #     ''' Access to database and fill the row '''

    #     file = open('./dates.db','a')
    #     file.write('%s|%s\n' % (date,time))
    #     file.close



    # def run_menu(self):
    #     ''' exec program '''

    #     sel = int(input('\nSelect option:\n\t(1) Check-in\
    #                             \n\t(2) Check-out\n'))

    #     if sel == 1:
    #         print('-- Check in --')
    #         action = 'checkin'
    #         datime = self.set_date_time()

    #         data = {
    #                 'action': action,
    #                 'date': datime 
    #             }
    #     elif sel == 2:
    #         print ('-- Check out --')
    #         action = 'checkout'
    #         datime = self.set_date_time()

    #         data = {
    #                 'action': action,
    #                 'date': datime 
    #             }
    #     else:
    #         print('err: option not found.')
    #         exit(1)

    #     return data


    # fill_row = insert_row(date,time)

    # ##

    # time_json = get_rows()
    # start_hour = time_json['start'].strip()
    # finish_hour = time_json['leave'].strip()
    
    # diff = time_diference(start_hour, finish_hour)

    # print('La diferencia entre la entrada y la salida es: %s' % diff)

