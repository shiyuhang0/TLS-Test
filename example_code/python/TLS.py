import MySQLdb
import sys
import platform

kwargs = {
}
kwargs["host"]=sys.argv[1]
kwargs["port"]=4000
kwargs["user"]=sys.argv[2]
kwargs["password"]=sys.argv[3]
kwargs["database"]="test"
kwargs["ssl"]={"ca": sys.argv[4]}
if platform.system() != 'Windows':
  kwargs['ssl_mode'] = "VERIFY_IDENTITY",
connection = MySQLdb.connect(**kwargs)

with connection:
  with connection.cursor() as cursor:
    cursor.execute("SELECT DATABASE();")
    m = cursor.fetchone()
    print(m[0])