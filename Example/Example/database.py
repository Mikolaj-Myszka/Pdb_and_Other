import sqlite3

connection = sqlite3.connect('myquotes.db')
cursor = connection.cursor()

# cursor.execute("""create table quotes_tb(
#     title text,
#     author text,
#     tag text
# )""")

cursor.execute("""insert into quotes_tb values(
    'Python is awesome', 'George', 'python')
""")

connection.commit()
connection.close()
