#!/usr/bin/env python3

from datetime import datetime
from registry.conf.settings import *

import os.path as path
import json
import sqlite3


#### DATA BASE ####

def open_connect(database):
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

def create_database(database):
    '''ensure database exists '''

    if not path.isfile(database):
        try:
            data_conn = open_connect(database)
            conn_db = data_conn['conn']
        except Exception as e:
            print(e)
        finally:
            conn_db.close()

def create_table(database, table, sql_table):
    ''' ensure table exists '''

    try:
        data_conn = open_connect(database)
        conn_db = data_conn['conn']
        cur = data_conn['cursor']
        make_table = sql_table % table
        cur.execute(make_table)
    except Error as e:
        print(e)
    finally:
        conn_db.close()

def insert_row(db_file, table_name, date, time, 
                action, work_diff, work_total):
    ''' insert a row '''

    #1. crear conexión + cursos
    data_conn = open_connect(db_file)
    conn_db = data_conn['conn']
    cur = data_conn['cursor']


    if conn_db is not None:
        cur.execute(query_in % (table_name, date,time, action, 
                                work_diff,work_total))
        conn_db.commit()
        conn_db.close()


def request_row(db_file, table_name, values={}):
    ''' request a row '''


#### Enyora tasks ####

def set_date_time():
    ''' Set current date '''

    date_time = {}
    
    date = datetime.today().strftime('%d-%m-%Y')
    time = datetime.now().strftime('%H:%M')

    date_time = { 'date': date, 'time': time }

    return date_time

def get_rows():

    file = open('./dates.db','r')
    lines = file.readlines()

    entrance = lines[0].split('|')[1]
    leave = lines[-1].split('|')[1]

    times = {'start': entrance, 'leave': leave}

    return times


def insert_file_row(date,time):
    ''' Access to database and fill the row '''

    file = open('./dates.db','a')
    file.write('%s|%s\n' % (date,time))
    file.close

def time_diference(start,finish):
    ''' set diff time '''

    time_format = "%H:%M"

    parse_start_hour = datetime.strptime(start, time_format)
    parse_finish_hour = datetime.strptime(finish, time_format)

    diff = parse_finish_hour - parse_start_hour

    return diff


def test_action(table_name, db_file, date, action):
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

def run_menu():
    ''' exec program '''

    sel = int(input('\nSelect option:\n\t(1) Check-in\
                            \n\t(2) Check-out\n'))

    if sel == 1:
        print('-- Check in --')
        action = 'checkin'
        datime = set_date_time()

        data = {
                'action': action,
                'date': datime 
            }
    elif sel == 2:
        print ('-- Check out --')
        action = 'checkout'
        datime = set_date_time()

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

