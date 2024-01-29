import sqlite3

connection = sqlite3.connect('laptime.db')


results = connection.execute('''
    SELECT manu.name, car2.model, car2.time
    FROM car2                        
    INNER JOIN manu ON manu.id = car2.manu_id
    INNER JOIN drive ON drive.id = car2.drive_id
    WHERE drive.id == 1
    ORDER BY car2.time ASC                         
''')

for row in results.fetchall():
    print(f'{row[0]} {row[1]} {row[2]}')

connection.close()