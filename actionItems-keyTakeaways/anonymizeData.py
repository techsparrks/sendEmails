import mysql.connector
from mysql.connector import Error
from db_connection import connect, close

def anonymize():
    try:
        connection = connect()
        if connection.is_connected():
            db_Info = connection.get_server_info()
            print("Connected to MySQL Server version ", db_Info)
            cursor = connection.cursor()
            cursor.execute("select database();")
            record = cursor.fetchone()
            print("You're connected to database: ", record)
            #print("Before updating a record ")
            sql_select_query = """select j.coachee_id from coachee_journey_bookings as j where journey_end_date <= CURDATE() and is_journey_complete is TRUE and j.program_id in (select program_id from programmes where program_end_date <= CURDATE()) """ 
            cursor.execute(sql_select_query)
            records = cursor.fetchall()
            print("Total rows are:  ", len(records))
            print("Printing each row")
            for row in records:
                #data = [faker.first_name(), faker.last_name(), faker.email(), faker.password(), faker.phone_number(), row[0]]
                data = ["unknown", "unkown", "unkown@unkown.com", "unknown", row[0]]
                sql_update_query="""UPDATE coachees SET first_name=%s, last_name=%s, email_id=%s, phone_number=%s WHERE coachee_id=%s"""
                cursor.execute(sql_update_query, data)
                connection.commit()
                print(cursor.rowcount, "record(s) affected")

            # records = cursor.fetchwarnings()
            print(records)

    except Error as e:
        print("Error while connecting to MySQL", e)
    
    finally:
        close(connection)
