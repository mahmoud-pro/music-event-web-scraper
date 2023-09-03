# import sqlite3
#
# connection = sqlite3.connect('data.db')
# cursor = connection.cursor()

# cursor.execute("INSERT INTO events VALUES ('Fest', 'Giza', '5.10.2023')")
# connection.commit()

# cursor.execute("SELECT band, date FROM events WHERE date = '5.10.2023'")

# new_data = [('ABC', 'Cairo', '5.10.2023'),
#             ('CDE', 'Qatar', '5.10.2023'),
#             ('ABC', 'Paris', '5.12.2023')]
#
# cursor.executemany("INSERT INTO events VALUES(?, ?, ?)", new_data)
# connection.commit()

# cursor.execute("SELECT * FROM events WHERE city = 'Cairo'")
#
# results = cursor.fetchall()
# print(results)



