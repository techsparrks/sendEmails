from db_connection import connect, close
import Error 

def check_coachee(coachee_email):
  try:
    connection = connect()
    if connection.is_connected():
      cursor = connection.cursor()
      sql_select_query = """select * from coachees as c where c.email_id=%s and c.email_id <> 'unknown' """ 
      cursor.execute(sql_select_query, [coachee_email])
      record = cursor.fetchall()
      if record:
        print("The coachee is still active since their journey and program where they belong to is still going-on. The coachee's personal data will be removed as soon as it ends.")
      else:
        print("the coachee personal data has been deleted")
           
  except Error as e:
    print("Error while connecting to MySQL", e)
    
  finally:
    close(connection)
    
