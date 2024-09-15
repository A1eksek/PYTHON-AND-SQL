import psycopg2

conn = psycopg2.connect(dbname='testdb1', user='postgres', password='1111', host='127.0.0.1', port='5432')
cursor = conn.cursor()

# cursor.execute('CREATE TABLE people (id SERIAL PRIMARY KEY, name VARCHAR(50), age INTEGER)')
# conn.commit() #подтверждение транкзации
# print('ТАБЛИЦА СОЗДАНА')
# conn.autocommit = True #используется для создания БД
# sql = 'CREATE DATABASE testdb1'
# cursor.execute(sql)
# print('База данных создана')
# bob = ('Алиса', 68)
# cursor.execute("INSERT INTO people(name, age) VALUES (%s, %s)", bob)
# people = [('Костя', 32), ('Маша', 12), ('Алексей', 16)]
# cursor.executemany("INSERT INTO people(name, age) VALUES(%s, %s)", people) #позваляет вставить набор строк
# conn.commit()

# cursor.execute("SELECT * FROM people")
# cursor.execute("SELECT * FROM people WHERE age > 30")
# print(cursor.fetchall())

# cursor.execute("SELECT * FROM people")
# for person in cursor.fetchall():
#     print(f"{person[1]} - {person[2]}")

# cursor.execute('SELECT * FROM people')
# print(cursor.fetchmany(3))
# print(cursor.fetchmany(2))

# cursor.execute('SELECT * FROM people')
# print(cursor.fetchone())

cursor.execute('SELECT * FROM people WHERE id = 2')
name, age = cursor.fetchone()
print(f'Name: {name} Age: {age}')


cursor.close()
conn.close()

"""
Метод cursor() объекта connection возращает cursor - объект cursor, через который можно отправлять запросы к бд.
Для этого класс cursor представляет ряд методов

1) execute(query, vars=None) - выполняет одну SQL инструкцию. Через второй параметр
"""
