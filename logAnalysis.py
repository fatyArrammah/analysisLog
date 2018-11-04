#!/usr/bin/env python3

import datetime
import psycopg2
import sys

DBNAME = "news"


# This function retrieves most popular three articles

def getMostArticle(db):
    c = db.cursor()
    query = """SELECT title,
                      COUNT(PATH) AS views
               FROM articles
               LEFT JOIN log ON PATH LIKE '%'||slug||'%'
               GROUP BY title
               ORDER BY 2 DESC
               LIMIT 3;"""
    c.execute(query)
    rows = c.fetchall()
    return rows


# This function retrieves most popular authors

def getMostAuthers(db):
    c = db.cursor()
    query = """SELECT name,
                      views
               FROM authors
               JOIN
                  (SELECT author,
                          COUNT(PATH) AS views
                   FROM articles
                   LEFT JOIN log ON PATH LIKE '%'||slug||'%'
                   GROUP BY 1
                   ORDER BY 2 DESC) log_views ON authors.id =
                   log_views.author;"""
    c.execute(query)
    rows = c.fetchall()
    return rows


# This function retrieves the day/s which has more than 1% of request error

def getDayOfError(db):
    c = db.cursor()
    query = """SELECT TO_CHAR(a.date_event, 'Month') month_part,
                      DATE_PART('day', a.date_event) day_part,
                      DATE_PART('year', a.date_event) year_part,
                      b.error_rate * 100.00/a.total error_rate
                FROM
                  (SELECT DATE(TIME) date_event,
                          COUNT(*) total
                   FROM log
                   GROUP BY 1) a
                JOIN
                  (SELECT DATE(TIME) date_event,
                          COUNT(*) error_rate
                   FROM log
                   WHERE status = '404 NOT FOUND'
                   GROUP BY 1) b ON a.date_event = b.date_event
                AND b.error_rate * 100.00/a.total > 1.0
                ORDER BY 1;"""
    c.execute(query)
    rows = c.fetchall()
    return rows


if __name__ == '__main__':
    # connect to the "news" database
    db = psycopg2.connect(database=DBNAME)
    # initialize txt file of the result
    file = open("logAnalysisResult.txt", "w")
    # write into txt file -----------------------------------------------
    file.write('Hello....\r\n')
    file.write("The result of news website log analysis .. \r\n")
    file.write("====================================================\r\n")
    file.write("1) The most popular three articles: \r\n")

    # reterive result of the first question
    POST = "\r\n* \"%s\" -- %s views"
    result = "".join(POST % (title, views) for title, views in
                     getMostArticle(db))
    file.write(result)
    file.write("\r\n")
    file.write("====================================================\r\n")
    file.write("2) The most popular authors: \r\n")

    # reterive result of the second question
    POST1 = "\r\n* %s -- %s views "
    result1 = "".join(POST1 % (name, views) for name, views in
                      getMostAuthers(db))
    file.write(result1)
    file.write("\r\n")
    file.write("====================================================\r\n")
    file.write("3) The day/s has more than 1% request error:   ")
    file.write("\r\n")
    # reterive result of the third question
    POST2 = "\r\n %0.5s%d, %d -- %03.2f%% errors "
    result2 = "".join(POST2 % (month_part, day_part, year_part, error_rate)
                      for month_part, day_part, year_part, error_rate in
                      getDayOfError(db))
    file.write(result2)
    file.write("\r\n")
    file.write("====================================================\r\n")
    # close txt file
    file.close()
    # close database connection
    db.close()
    # write the result into the terminal -------------------------------------
    sys.stdout.write("---------------------------------------------------\r\n")
    sys.stdout.write("Hello....\r\n")
    sys.stdout.write("The result of news website log analysis .. \r\n")
    sys.stdout.write("---------------------------------------------------\r\n")
    sys.stdout.write("\r\n")
    sys.stdout.write("1) The most popular three articles: \r\n")
    sys.stdout.write(result)
    sys.stdout.write("\r\n\r\n")
    sys.stdout.write("---------------------------------------------------\r\n")
    sys.stdout.write("\r\n")
    sys.stdout.write("2) The most popular authors: \r\n")
    sys.stdout.write(result1)
    sys.stdout.write("\r\n\r\n")
    sys.stdout.write("---------------------------------------------------\r\n")
    sys.stdout.write("\r\n")
    sys.stdout.write("3) The day/s has more than 1% request error:   ")
    sys.stdout.write("\r\n")
    sys.stdout.write(result2)
    sys.stdout.write("\r\n\r\n")
    sys.stdout.write("---------------------------------------------------\r\n")
