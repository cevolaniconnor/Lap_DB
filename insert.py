import sqlite3

# Connect to the SQLite database
connection = sqlite3.connect('laptime.db')

# Add a new column engine_id as a foreign key from the engine table
update_query = '''
    UPDATE car2
    SET model = "911 GT2 RS 991.2 2018"
    WHERE id = 5; 
'''
connection.execute(update_query)
connection.commit()

# Close the connection
connection.close()







"""
import sqlite3

connection = sqlite3.connect('laptime.db', check_same_thread=False, isolation_level=None)

cursor = connection.cursor()

# Insert statement for engine table
insert_engine_statement = "INSERT INTO engine (desc) VALUES (?)"
# Values to insert for engine table
values_engine = [("Front Engined",),
                 ("Mid Engined",),
                 ("Rear Engined",)]

# Execute the insert statement for engine table
cursor.executemany(insert_engine_statement, values_engine)

# Commit the changes to the database
connection.commit()

# Close the connection
connection.close()
"""