Enyora Registry
###############

Record the time of entry and exit in the office. Calculate the hours worked daily, weekly and monthly.

Install
*******

.. code:: console

  $ git clone https://github.com/nebul4ck/rhea-credentials-manager-client.git
  $ apt install ./enyora/enyora-0.0.1.deb

..


Configure
*********

.. code:: console

  $ sudo vi /etc/enyora/enyora.conf
  [database]
  enyora_db = '~/.enyora.db'
  enyora_table = 'enyora_registry'
..

.. tip::

  Default values are recommended
..

Use
===

.. code:: console

  $ buanaclient -h
  usage: enyora [-h] [-a {in,out,day,week,month}]

  Enyora registry.

  optional arguments:
    -h, --help            show this help message and exit
    -a {in,out,day,week,month}, --action {in,out,day,week,month}
                          in|out to record entry or exit time. unit time to show
                          about worked hours.

    EXAMPLES
    
      $ enyora -a in (sets the entry time)
      $ enyora -a out (sets the exit time)
      $ enyora -a day (show daily worked hours)
      $ enyora -a week (show weekly worked hours)
      $ enyora -a month (show montly worked hours)
..