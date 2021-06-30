def get_hs():
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

    query = ("SELECT username,score from snake_highscores ORDER BY score DESC LIMIT 5")


    cursor.execute(query)

    scores = {}
    i = 0
    for (username, score) in cursor:
        scores[i] = {"name":username,"score":score}
        i+=1
        # print("{}, Score: {} was achieved on {:%d %b %Y %H:%M}".format(username, score, date))
    print(scores)
    cursor.close()
    cnx.close()
    return scores