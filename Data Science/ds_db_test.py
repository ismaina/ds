import numpy as np
import pandas as pd
import mysql.connector
from mysql.connector import errorcode

query = ''
mysql_driver = 'mysql+pymsql'
mysql_server = '35.243.166.3'
mysql_uname = 'user3'
mysql_pwd = '123456'
mysql_host = 'localhost'
mysql_port = '3306'
mysql_db = 'safaricom_2019'
db_conn = mysql.connector
my_courses =[]
students = []
course = []

def enterqury():
    q = str(input("Enter your sql query: "))
    if len(q) != 0:
        try:
            make_connection(q)
        except mysql.connector.Error as err:
            return('We have encountered this error {}\n'.format(err))
    else:
        print('Enter some Data')


def make_connection(q):
    query = q
    dbconnect = db_conn.connect (
        host = mysql_server,
        user = mysql_uname,
        passwd = mysql_pwd,
        database = mysql_db    
    )
    if dbconnect:
        print("Success!!!")
        mycursor = dbconnect.cursor()
        #query = "show tables"
        mycursor.execute(query)
        myresult = mycursor.fetchall()
        print("______________Start of output____________\n")
        for x in myresult:
            print(x)
            my_courses.append(x)

        print("______________End of output____________\n")
        mycursor = dbconnect.cursor()
        query = "SELECT * FROM students"
        mycursor.execute(query)
        myresult = mycursor.fetchall()
        for y in myresult:
            print(y)
            students.append(y)

        mycursor = dbconnect.cursor()
        query = "SELECT * FROM courses"
        mycursor.execute(query)
        myresult = mycursor.fetchall()
        for y in myresult:
            print(y)
            course.append(y)
        mycursor.close()

        print("Connection has been closed !!!")
        for num in range(len(students)):
            n = students[num][1]  # get student name
            #Scs = int(students[num][0])
            #print(n,course[cs][1])
            cs = my_courses[num][2] # get student course IDs
            print('----',n,"=> course is ", cs,"project =>", my_courses[num][3], "\n\n")
            #print(course[cs][1])
            #print(n,"project =>", my_courses[num][3], "\n\n")

    else:
        print("Error in connection")


age = int(input("Enter Age:"))

if age >=24 :
    print('You are an adult. Welcome to the game')
    enterqury()
else:
    print('You are not old enough to do data science')
