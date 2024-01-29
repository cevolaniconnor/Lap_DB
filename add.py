import sqlite3

def insert_car():

    try:
        model = input("Car Model Name: ")
        time = input("Lap Time: ")
        manu_id = int(input("Manufacturer ID: "))
        drive_id = int(input("Drivetrain type: "))
        engine_id = int(input("Engine layout: "))

        conn = sqlite3.connect('laptime.db', check_same_thread=False, isolation_level=None) 

        sql = """ INSERT INTO car2
            (model, time, manu_id, drive_id)
            VALUES ('{}', '{}', '{}', '{}', '{}');""".format(model, time, manu_id, drive_id, engine_id)
    
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()
        print("Successful Insert!")
        cursor. close()

    except sqlite3. Error as e:
        print ("Error while Inserting Data", e) 

    finally:
        if (conn):
            conn. close ()
            print ("Connection Closed")