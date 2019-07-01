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


import ast

from enyora.conf.settings import baseConf
from enyora.conf.cod_messages import cod_10, \
    cod_11
from enyora.lib.actions import registryAction

class Base(object):
    """Base class."""
    def __init__(self):
        super(Base, self).__init__()
        #self.name=self.__class__.__name__

        ''' Loading config parameters '''
        loadConf=baseConf()
        self.config=loadConf.Conf()

        ''' Loading Enyora Registry Actions '''
        self.registry_action=registryAction(self.config)

    def run(self, param):

        ''' Ensure database and table exists '''
        self.registry_action.check_config()

        # TODO improve select/case
        if param=='in' or param=='out':
            ''' Insert new record '''
            self.registry_action.clocking(param)
        elif param=='today' or \
            param=='week' or \
            param=='month' or \
            param=='year':
            ''' Show info: worked hours '''
            show_worked=self.registry_action.show_worked_hours(param)
            print(cod_11 % (param, show_worked))
            exit(0)
        else:
            print(cod_10)
            exit(1)

