import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

db_user = os.environ.get("DB_USER")
db_host = os.environ.get("DB_HOST")
db_password = os.environ.get("DB_PASSWORD")
db_db = os.environ.get("DB_DB")

cnx = mysql.connector.connect(user=db_user, password=db_password,
                              host=db_host,
                              database=db_db)
cursor = cnx.cursor()

query = ("SELECT * from snake_highscores")


cursor.execute(query)

for (id, username, score,date) in cursor:
  print("[{}] {}, Score: {} was achieved on {:%d %b %Y %H:%M}".format(
    id, username, score, date))

cursor.close()
cnx.close()