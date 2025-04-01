import sqlite3
connection = sqlite3.connect('database1.db')
cur = connection.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS 'employees' (
	'id_employee' INTEGER PRIMARY KEY AUTOINCREMENT,
	'name' TEXT,
	'email' TEXT,
	'phone_number' TEXT,
	'position' TEXT,
	'department' TEXT
)""")


cur.execute("""CREATE TABLE IF NOT EXISTS 'clients' (
	'id_client' INTEGER PRIMARY KEY AUTOINCREMENT,
	'name' TEXT,
	'email' TEXT,
	'phone_number' TEXT,
	'passport' TEXT
)""")


cur.execute("""CREATE TABLE IF NOT EXISTS 'things' (
	'id_thing' INTEGER PRIMARY KEY AUTOINCREMENT,
	'count' INTEGER,
	'price' INTEGER,
    'insurance' BLOB,
	'weight' INTEGER,
	'oversized' BLOB,
	'client_id' INTEGER
)""")


cur.execute("""CREATE TABLE IF NOT EXISTS 'contracts' (
	'id_contract' INTEGER PRIMARY KEY AUTOINCREMENT,
	'number' TEXT,
	'date' TEXT,
	'start_price' INTEGER,
	'discount' INTEGER,
	'deal_status' BLOB,
	'finish_price' INTEGER,
	'address_start' TEXT,
	'address_finish' TEXT,
	'thing_id' INTEGER UNIQUE,
	'client_id' INTEGER,
	'employee_id' INTEGER
)""")


cur.execute("""CREATE TABLE IF NOT EXISTS 'reports' (
	'id_report' INTEGER PRIMARY KEY AUTOINCREMENT,
	'number' TEXT,
	'date' TEXT,
	'report_type' TEXT,
	'description' TEXT,
	'employee_id' INTEGER
)""")





""""
# Добавление данных в таблицы
employees = [
    ('Иванов Иван Иваныч', 'ivan@example.com', '+79017171552', 'Инженер', 'Технический отдел'),
    ('Петров Петр Петрович', 'petr@example.com', '+79039345678', 'Менеджер', 'Отдел приема заказов'),
    ('Кузнецова Анна Андреевна', 'anna@example.com', '+79032341234', 'Аналитик', 'Логистический отдел')
]
cur.executemany("INSERT INTO 'employees' (name, email, phone_number, position, department) VALUES (?, ?, ?, ?, ?)", employees)

#_______________________________________________________________________


clients = [
    ('Смирнова Мария Александровна', 'maria@example.com', '+79033335432', '1234789321'),
    ('Соколов Алексей Сергеевич', 'alexey@example.com', '+79032223211', '9083465863'),
    ('Орлова Ольга Геориевна', 'olga@example.com', '+79017895678', '9374658325'),
    ('ffsf', 'olga@example.com', '+79017895678', '9374658325')
]
cur.executemany("INSERT INTO 'clients' (name, email, phone_number, passport) VALUES (?, ?, ?, ?)", clients)
#_______________________________________________________________________



things = [
    (10, 2999, None, 15, False,1),
    (5, 4999, None, 25, False,2),
    (20, 1599, None, 10, False,3)
]
cur.executemany("INSERT INTO 'things' (count, price, insurance, weight, oversized, client_id) VALUES (?, ?, ?, ?, ?, ?)", things)


#____________________________________________________________________



contracts = [
    ('ДОГ12345', '2024-05-18', 50000, 5, False, 47500, 'ул. Ленина, д. 10', 'ул. Победы, д. 20', 1, 1, 1),
    ('ДОГ54321', '2024-06-10', 30000, 10, None, 27000, 'ул. Гагарина, д. 5', 'ул. Космонавтов, д. 15', 2, 2, 2),
    ('ДОГ67890', '2024-07-25', 15000, 15, None, 12750, 'ул. Трудовая, д. 1', 'ул. Молодежная, д. 2', 3, 3, 3)
]
cur.executemany("INSERT INTO 'contracts' (number, date, start_price, discount, deal_status, finish_price, address_start, address_finish, thing_id, client_id, employee_id) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", contracts)



#_______________________________________________________________
reports = [
    ('ОТЧ67890', '2024-05-18', 'Перевозки', 'Отчет', 1),
    ('ОТЧ54321', '2024-06-10', 'Перевозки', 'Отчет', 2),
    ('ОТЧ12345', '2024-07-25', 'Перевозки', 'Отчет', 3)
]
cur.executemany("INSERT INTO 'reports' (number, date, report_type, description, employee_id) VALUES (?, ?, ?, ?, ?)", reports)

#_______________________________________________________________________
"""

connection.commit()
connection.close()