# -*- coding: utf8 -*-

"""
.. module:: base
   :platform: Unix/Linux
   :synopsis: Initialize Enyora
.. moduleauthor::
   :Author: nebul4ck
   :mail: a.gonzalezmesas@gmail.com
   :Web : https://www.linkedin.com/in/nebul4ck/
   :Version : 0.0.1
"""




from registry.conf.settings import Conf

def Base():

    ''' ensure en_registry database exists '''
    create_database(enyora_db)

    ''' ensure enyora table exists '''
    create_table(enyora_db, enyora_table, sql_enyora_table)

    ''' return inputs menu values '''
    data_menu = run_menu()
    datime = data_menu['date']
    date = datime['date']
    time = datime['time']
    action = data_menu['action']

    ''' insert new input '''
    

    ''' compare action '''
    try:
        status_action = test_action(table_name, db_file, date, action)
        # sacar variables de aqui ya que es la última row, por ejemplo la fecha,
        # la hora, y la work diference
    except Exception as e:
        print('Se haa habido un error')

    if status_action:
        print('No es posible realizar dos acciones iguales de forma \
                consecutiva.')
    elif status_action == None:
        print('añadimos un registro nuevo')
        insert_row(db_file, table_name, date, time, 
                action, '', '')
    else:
        # 1. como tenemos la hora de la ultima row, hacer la diferencia entre la nueva y la anterior
        # 2. PODEMOS QUITAR EL WORK TOTAL Y HACER UNA CONSULTA ONFLY CADA VEZ QUE QUERAMOS LAS HORAS TOTALES DE UN DIA
        # ESTO SE PUEDE HACER SUMANDO TODAS LAS DIFF PARA NA FECHA DADA.
        # TAMBIEN PUEDO METER UNA SUMA DE TODAS LAS DIFERENCIAS HASTA EL MOMENTO E IR ALMACENANDOLA EN EL CAMPO TOTAL
        # Y CADA VEZ QUE QUIERA PERGUNTAR POR EL TOTAL IRME A LA ULTIMA ROW DE ESE DIA
        print('son diferente, diff + total + insert')
        calc_diff_total = calc_work()

if __name__ == '__main__':
    main()


enyora_config = Base()
print(ast.literal_eval(enyora_config['database']['enyora_db']))