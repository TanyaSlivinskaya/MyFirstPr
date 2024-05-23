"""Представим, что у нас есть таблица "Employees" с полями "Name", "Position", "Department", "Salary".
• +Создайте таблицу "Employees" с указанными полями.
• +Вставьте в таблицу несколько записей с информацией о сотрудниках вашей компании.
• +Измените данные в таблице для каких-то сотрудников. Например, изменим должность одного из сотрудников на более высокую.
• +Добавьте новое поле "HireDate" (дата приема на работу) в таблицу "Employees".
• +Добавьте записи о дате приема на работу для всех сотрудников.
• +Найдите всех сотрудников, чья должность "Manager".
• +Найдите всех сотрудников, у которых зарплата больше 5000 долларов.
• +Найдите всех сотрудников, которые работают в отделе "Sales".
• +Найдите среднюю зарплату по всем сотрудникам.
• +Удалите таблицу "Employees"""
import sqlite3

connection = sqlite3.connect("14.1_employees")
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Employees(
Name TEXT NOT NULL,
Position TEXT NOT NULL,
Department TEXT NOT NULL,
Salary INTEGER
)
""")

employees = [
    ('Anna', 'Developer', 'IT', 5000),
    ('Bob', 'Manager', 'Sales', 2000),
    ('Dima', 'Manager', 'Sales', 1500),
    ('Nadya', 'Manager', 'IT', 3200)
]

cursor.executemany('''
INSERT INTO Employees (Name, Position, Department, Salary) VALUES (?, ?, ?, ?)
''', employees)
connection.commit()

cursor.execute('UPDATE Employees SET Position = ? WHERE name = ?', ("Manager", 'Anna'))

connection.commit()

cursor.execute(''' ALTER TABLE Employees ADD COLUMN HireDate TEXT
''')


hire_dates = [
    ('05.03.2020', 'Anna'),
    ('08.07.2019', 'Bob'),
    ('15.02.2013', 'Dima'),
    ('16.06.2023', 'NadyA')
]

cursor.executemany('''
UPDATE Employees SET HireDate = ? WHERE Name = ?
''', hire_dates)
connection.commit()

cursor.execute('SELECT name, Position FROM Employees WHERE Position = ?', ("Manager",))
results_pos = cursor.fetchall()

for result in results_pos:
    print(result)

cursor.execute('SELECT name, Salary FROM Employees WHERE Salary = ?', (5000,))
results_sal = cursor.fetchall()


for result in results_sal:
    print(result)

cursor.execute('SELECT name, Department FROM Employees WHERE Department = ?', ("Sales",))
results_dep = cursor.fetchall()

for result in results_dep:
    print(result)

cursor.execute('SELECT AVG(Salary) FROM employees')
average_salary = cursor.fetchone()[0]

cursor.execute(''' DROP TABLE Employees ''')
connection.commit()

connection.close()