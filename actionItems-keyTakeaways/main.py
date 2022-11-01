from db_connection import connect, close
from anonymizeData import anonymize
from check_coachee import check_coachee

if __name__ == '__main__':
  check_coachee('lala@lala.com')
  anonymize()
