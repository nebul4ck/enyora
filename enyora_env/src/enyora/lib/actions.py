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

from datetime import datetime


class registryAction(object):
    """Registry class"""
    def __init__(self):
        self.name=self.__class__.__name__

    def set_date_time(self):
        ''' Set current date '''

        date_time = {}
        
        date = datetime.today().strftime('%d-%m-%Y')
        time = datetime.now().strftime('%H:%M')

        date_time = { 'date': date, 'time': time }

        return date_time

    def get_rows(self):

        file = open('./dates.db','r')
        lines = file.readlines()

        entrance = lines[0].split('|')[1]
        leave = lines[-1].split('|')[1]

        times = {'start': entrance, 'leave': leave}

        return times


    def insert_file_row(self, date, time):
        ''' Access to database and fill the row '''

        file = open('./dates.db','a')
        file.write('%s|%s\n' % (date,time))
        file.close

    def calc_work(self, start_time, finish_time):
        ''' set diff time '''

        time_format = "%H:%M"

        parse_start_hour = datetime.strptime(start_time, time_format)
        parse_finish_hour = datetime.strptime(finish_time, time_format)

        diff = parse_finish_hour - parse_start_hour

        return diff

    def test_action(self, table_name, db_file, date, action):
        ''' ensure that the last action reg is not like
            the current 

            action reg = checkin|checkout 
        '''

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

    def run_menu(self):
        ''' exec program '''

        sel = int(input('\nSelect option:\n\t(1) Check-in\
                                \n\t(2) Check-out\n'))

        if sel == 1:
            print('-- Check in --')
            action = 'checkin'
            datime = self.set_date_time()

            data = {
                    'action': action,
                    'date': datime 
                }
        elif sel == 2:
            print ('-- Check out --')
            action = 'checkout'
            datime = self.set_date_time()

            data = {
                    'action': action,
                    'date': datime 
                }
        else:
            print('err: option not found.')
            exit(1)

        return data






            # fill_row = insert_row(date,time)

            # ##

            # time_json = get_rows()
            # start_hour = time_json['start'].strip()
            # finish_hour = time_json['leave'].strip()
            
            # diff = time_diference(start_hour, finish_hour)

            # print('La diferencia entre la entrada y la salida es: %s' % diff)

