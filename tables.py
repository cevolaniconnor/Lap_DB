import sqlite3

connection = sqlite3.connect('laptime.db', check_same_thread=False, isolation_level=None)

connection.execute('''
    CREATE TABLE IF NOT EXISTS manu(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name Text
                )
                ''')

connection.execute('''
     CREATE TABLE IF NOT EXISTS car2(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                model TEXT,
                time TEXT,
                manu_id INTEGER,
                FOREIGN KEY(manu_id) REFERENCES manu(id)
                )              
                ''')

connection.execute('''
    CREATE TABLE IF NOT EXISTS drive(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                desc TEXT)
                ''')

connection.execute('''
    CREATE TABLE IF NOT EXISTS engine(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                desc TEXT)     
                   ''')

results = connection.execute('''
    SELECT car2.id, model, engine.desc
    FROM car2  
    LEFT JOIN engine ON engine.id = car2.engine_id;
''')
connection.commit
# Print the results
for row in results.fetchall():
    print(f'{row[0]} {row[1]} {row[2]}')
    
connection.close()


