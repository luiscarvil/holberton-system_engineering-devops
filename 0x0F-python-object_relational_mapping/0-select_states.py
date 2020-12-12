#!/usr/bin/python3
""" import and print database MySQL """
import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        password=argv[2],
        db=argv[3]
    )
    cur = db.cursor()
    rows = cur.execute("SELECT * FROM states ORDER BY states.id")
    for i in range(rows):
        print(cur.fetchone())
    cur.close()
