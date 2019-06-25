TO-DO
#####

1. argparse: import/export excel format. 
**ie:**

.. code:: console

  enyora --import foo.{xls,xlsx,xlsm,xml}
  enyora --export bar.{xls,xlsx,xlsm,xml}
..

2. Show worked hours in a day, a week and a month
**ie:**

..code:: console

  enyora --show day
..

4. Multi-tenant

5. Multi-user

6. Holidays control
**ie:**

if a worker going to clock-in a new entry-point and the latest worked day was few days ago, he have to define the days worked and not (holidays/vacances).

7. User/worker profile.
**ie:**

Worked hours, work schedule, holidays, taking a sick leave and more

8. Front-end

9. AWS migration (HA, auto-scaling)

10. logger?

11. Show menu needs a method that check if the values inserting are a correct format

13. argsparte does not check if the arg is -a -an -asdddsd --action --atusas, etc.. (only -a or --action is permit)

14. sqlite> SELECT * FROM enyora_registry WHERE r_date LIKE '%2019-06-25%';
14|2019-06-25 00:16:38|out|2:00:00
15|2019-06-25 18:40:59|in|

15. Hacer que todo termine en base.py e imprimirlo desde ahí
