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
    -a {in,out}, --action {in,out}   registry clock-in or clock-out at office
    -s {today,week,month,year}, --show {today,week,month,year} show worked hours per day/week/month/year
                          

    EXAMPLES
    
      $ enyora -a|--action in
      $ enyora -a|--action out
      $ enyora -s|--show today
      $ enyora -s|--show week
      $ enyora -s|--show month
      $ enyora -s|--show year
..
