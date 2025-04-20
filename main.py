# import sqlite3 as sq


# conn = sq.connect('db..sql')
# cursor = conn.cursor()
# tableName = "word"
# cursor.execute(f"""
# CREATE TABLE {tableName}
# name TEXT,
# namber INTEGER

# """
# )
# data = ('bilol',13),('nura',23)('lola',12)



# conn.commit()
# conn.close()
# print("ok")

# import sqlite3 as sql


# conn = sql.connect("db.sql")
# cursor = conn.cursor()

# tableName = "Persons"
# cursor.execute(
# f"""
# SELECT  * FROM  {tableName}   
# ORDER BY age DESC

# """
# )

# for i in cursor.fetchall():
#     print(i)

# conn.commit()
# conn.close()
    

# import sqlite3 as sql 

# conn = connect('users.db')
# cursor = conn.cursor()

# # Создание таблицы, если её нет
# cursor.execute(f"""
# CREATE TABLE IF NOT EXISTS users
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     name TEXT NOT NULL,
#     email TEXT NOT NULL UNIQUE
# """"
# )
# a = int(input())
# b = int(input())
# print(a+b)


# N = 10
# b =  N * (N + 1)  //2
# print(f"сумма чисел равен от 1 до {N} равен включительно: {b} ")



# n = int(input("Введите число, оканчивающееся на 5 "))
# print(f"{n}*2")






# a = input().strip()
# b = input().strip()

# shifts = set()
# for i in range(len(b)):
#     shifted = b[i:] + b[:i]
#     shifts.add(shifted)

# count = 0
# len_b = len(b)
# for i in range(len(a) - len_b + 1):
#     substring = a[i:i+len_b]
#     if substring in shifts:
#         count += 1

# print(count)


