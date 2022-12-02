import MySQLdb
import sys

connection = MySQLdb.connect(

  host= sys.argv[1],
  port=4000,
  user=sys.argv[2],
  password=sys.argv[3],
  database="test",
  ssl_mode="VERIFY_IDENTITY",
  ssl={
    "ca": sys.argv[4]
  }
)

with connection:
  with connection.cursor() as cursor:
    cursor.execute("SELECT DATABASE();")
    m = cursor.fetchone()
    print(m[0])