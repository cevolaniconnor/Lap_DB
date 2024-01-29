import sqlite3

def retrieve_laptime_data():
    connection = sqlite3.connect('laptime.db', check_same_thread=False, isolation_level=None)

    try:
        results = connection.execute('''
            SELECT manu.name, car2.model, car2.time
            FROM car2
            INNER JOIN manu ON manu.id = car2.manu_id
            ORDER BY car2.time ASC
        ''')

        center = "Laguna Seca - FULL"
        terminal_width = 80
        centered_text = center.center(terminal_width)

        connection.commit()

        print(centered_text)
        print("-"*79)
        for row in results.fetchall():
            print(f'{row[0]} {row[1]} - {row[2]}')

    finally:
        connection.close()

def retrieve_manu_data():
    connection = sqlite3.connect('laptime.db', check_same_thread=False, isolation_level=None)

    try:
        results = connection.execute('''
            SELECT manu.id, manu.name
            FROM manu
        ''')

        connection.commit()

        for row in results:
            print(f'{row[0]} {row[1]}')

    finally:
        connection.close()    


