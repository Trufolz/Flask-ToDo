import sqlite3


def execute_query(query, arguments=()):
    path = 'models/todo.db'
    connection = sqlite3.connect(path)
    cursor = connection.cursor()
    cursor.execute(query, arguments)
    data = cursor.fetchall()
    connection.commit()
    connection.close()

    return data

def create_table_query():
    query = """CREATE TABLE IF NOT EXISTS `todo` (
	          `id`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	          `name`	TEXT,
	          `status`	INTEGER);"""
    execute_query(query)

def select_all_query():
    query = """SELECT * FROM todo"""
    result = execute_query(query)

    return result

def select_by_id_query(id):
    query = """SELECT * FROM todo WHERE id = ?"""
    arguments = (id,)
    result = execute_query(query, arguments)

    return result

def add_query(name, status):
    query = """INSERT INTO todo (name, status) VALUES (?, ?)"""
    arguments = (name, status,)
    execute_query(query, arguments)

def edit_query(id, name, status):
    query = """UPDATE todo SET name = ?, status = ? WHERE id = ?"""
    arguments = (name, status, id,)
    execute_query(query, arguments)

def delete_query(id):
    query = """DELETE FROM todo WHERE id = ?"""
    arguments = (id,)
    execute_query(query, arguments)

def toggle_query(id, status):
    query = """UPDATE todo SET status = ? WHERE id = ?"""
    arguments = (status, id,)
    execute_query(query, arguments)

