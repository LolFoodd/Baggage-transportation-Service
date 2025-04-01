

import sqlite3
from tabulate import tabulate



def get_db_connection():
    conn = sqlite3.connect('database1.db')
    conn.row_factory = sqlite3.Row
    return conn


def fetch_and_print_contract(id):
    conn = get_db_connection()
    cursor = conn.cursor()

    query = """SELECT * FROM contracts, clients, employees
               WHERE contracts.client_id = clients.id_client and 
                     contracts.employee_id = employees.id_employee and
                     contracts.id_contract = ?"""

    # Выполнение запроса
    cursor.execute(query, (id,))
    rows = cursor.fetchall()

    if rows:
        # Получаем названия столбцов
        col_names = [description[0] for description in cursor.description]

        # Формируем список для таблицы, включая названия столбцов
        table_data = [col_names] + rows

        # Печатаем таблицу
        print(tabulate(table_data, headers="firstrow", tablefmt="fancy_grid"))
    else:
        print("No results found.")

    # Закрываем соединение
    conn.close()


# Пример использования функции
fetch_and_print_contract(1)
