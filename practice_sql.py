# -*- coding: utf-8 -*-

'!pip install psycopg2'

import psycopg2
import pandas as pd
 
DB_HOST = str(input('Введите хост'))
DB_USER = str(input('Введите хпользователя'))
DB_USER_PASSWORD = str(input('Введите пароль'))
DB_NAME = str(input('Введите имя базы'))

conn = psycopg2.connect(host=DB_HOST, user=DB_USER, password=DB_USER_PASSWORD, dbname=DB_NAME)
pd.read_sql_query("select * from customer", conn)

"""### Задание 1
Выбрать коды всех городов, в которых расположены отделы фирмы.
"""

pd.read_sql_query("""
SELECT DISTINCT
  location_id
FROM department
""", conn)

"""### Задание 2
Для каждого сотрудника определить, какой процент по отношению к зарплате составляют его комиссионные.
"""

pd.read_sql_query("""
SELECT last_name, commission/salary * 100
FROM employee
""", conn)

pd.read_sql_query("""
SELECT last_name, commission/salary * 100
FROM employee
WHERE commission IS NOT NULL
""", conn)

pd.read_sql_query("""
SELECT last_name, COALESCE(commission, 0)/salary * 100
FROM employee
""", conn)

"""### Задание 3
Вывести два инициала (с точками) и фамилии всех сотрудников, например:
"""


pd.read_sql_query("""
SELECT CONCAT(SUBSTR(first_name, 1, 1), '.') AS i1,
       CONCAT(middle_initial, '.') AS i2,
       last_name
FROM employee
""", conn)

"""### Задание 4
По каждой сделке вывести точную сумму сделки, сумму сделки, округленную в большую сторону, округленную в меньшую сторону, округленную по общепринятым правилами округления.
"""


pd.read_sql_query("""
SELECT  order_id,
        total,
        FLOOR(total),
        CEIL(total),
        ROUND(total)
from sales_order
""", conn)

"""### Задание 5
Выбрать фамилии всех сотрудников, у которых комиссионные больше зарплаты.
"""

pd.read_sql_query("""
SELECT last_name
FROM employee
WHERE commission > salary
""", conn)

"""### Задание 6
Выбрать фамилии всех сотрудников, фамилии которых начинаются на букву 'S'.
"""

pd.read_sql_query('''
SELECT last_name
FROM employee
WHERE last_name LIKE 's%'
''', conn)

"""### Задание 7
Выбрать имена всех сотрудников, которые не являются менеджерами (job_id=671) и не работают в отделе SALES в NEW YORK (department_id=13).
"""

pd.read_sql_query('''
SELECT *
FROM employee
WHERE job_id != 671 AND department_id != 13
''', conn)

"""### Задание 8
Выбрать фамилии всех сотрудников, у которых код должности 670 или 677 (CLERK или SALESPERSON).
"""

pd.read_sql_query('''
SELECT last_name, job_id
FROM employee
WHERE job_id IN (670, 677)
''', conn)

"""### Задание 9
Выбрать всех сотрудников, имена которых состоят из 6 букв и начинаются на 'MAR'.
"""

pd.read_sql_query('''
SELECT first_name
FROM employee
WHERE first_name LIKE 'MAR___'
''', conn)

"""### Задание 10
Выбрать фамилии всех сотрудников, которые поступили на работу после 15 апреля 1985 года.
"""

pd.read_sql_query('''
SELECT last_name 
FROM employee
WHERE hire_date > '1985-04-15'
''', conn)

"""### Задание 11
Выбрать фамилии всех сотрудников, которые поступили на работу в 1985 году.
"""

pd.read_sql_query('''
SELECT last_name
FROM employee
WHERE hire_date BETWEEN '1985-01-01' AND '1985-12-12'
''', conn)

"""### Задание 12
Для каждого сотрудника выбрать количество полных лет работы в фирме.
"""

pd.read_sql_query('''
SELECT first_name, last_name,
 EXTRACT(YEAR FROM AGE(hire_date))
FROM
 employee
''', conn)

"""### Задание 13
Выбрать количество сотрудников, получающих комиссионные. Если сотрудник получает 0 комиссионных, то это тоже считается. Не считаются только NULL.
"""

pd.read_sql_query("""
SELECT COUNT(*)
FROM employee
WHERE commission IS NOT NULL
""", conn)

pd.read_sql_query("""
SELECT COUNT(commission)
FROM employee
""", conn)

"""### Задание 14
Выбрать количество и общую сумму сделок, совершенных с покупателем, код которого - 104.
"""

pd.read_sql_query('''
SELECT
  COUNT(order_id) AS CountOrder, SUM(total) AS SumTotal
FROM 
  sales_order
WHERE
  customer_id = 104
''', conn)

"""### Задание 15
Выбрать среднюю зарплату по каждой должности.
"""

pd.read_sql_query('''
SELECT
  job_id, AVG(salary) AS avg_job
FROM 
  employee
GROUP BY job_id

''', conn)

"""### Задание 16
Выбрать среднюю зарплата продавцов (код должности - 670).
"""

pd.read_sql_query('''
SELECT
  job_id, AVG(salary)
FROM 
  employee
GROUP BY job_id
HAVING job_id = 670 
''', conn)

"""### Задание 17
 Выбрать средние зарплаты продавцов (код должности - 670) и клерков (код должности - 667).
"""

pd.read_sql_query('''
SELECT
  job_id, AVG(salary)
FROM
  employee
GROUP BY job_id
HAVING job_id IN (670, 667)
''', conn)

"""### Задание 18
Выбрать коды продуктов, по которым было совершено меньше 10 продаж.


"""

pd.read_sql_query('''
SELECT 
  product_id, COUNT(order_id)
FROM 
  item
GROUP BY product_id
HAVING COUNT(order_id) < 10
''', conn)

"""### Задание 19
Выбрать максимальную зарплату продавцов (код должности - 670) по каждому отделу.
"""

pd.read_sql_query('''
SELECT
  department_id, MAX(salary)
FROM employee
WHERE job_id = 670
GROUP BY department_id
''', conn)

"""### Задание 20
Выбрать список сотрудников фирмы в алфавитном порядке.
"""

pd.read_sql_query('''
SELECT 
  first_name, last_name
FROM employee
ORDER BY first_name
''', conn)
