Enyora Registry
###############

Record the time of entry and exit in the office. Calculate the hours worked daily, weekly and monthly.


Make package
************

In order to make a new DEBIAN package (enyora-x.y.z.deb) after to re-factor the src/ code, you must run make-package script.

.. code:: console

  $ ./make-package.sh 3.5 local enyora

  3.5: python_version
  local: make_mode
  enyora: repository name
..

Install
*******

.. code:: console

  $ git clone https://github.com/nebul4ck/enyora.git
  $ apt install ./enyora-0.0.1.deb
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