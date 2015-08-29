import MySQLdb

HOST_NAME = "hechabra.cgsjxh1gdjac.us-west-2.rds.amazonaws.com"
USER_NAME = "pete7863"
PASSWORD = "Nalex1391!"
DATABASE = "hechabra"

db = None

def init():
    global db

    db = MySQLdb.connect(host=HOST_NAME,
                         user=USER_NAME,
                         passwd=PASSWORD,
                         db=DATABASE)

def get_cursor():
    global db

    try:
        return db.cursor()
    except:
        db = MySQLdb.connect(host=HOST_NAME,
                         user=USER_NAME,
                         passwd=PASSWORD,
                         db=DATABASE)
        return db.cursor()



def perform_query(query):
    cur = get_cursor()
    cur.execute(query)

    return cur.fetchall()