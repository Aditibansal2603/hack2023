import sqlite3

#connecting to sqlite
conn = sqlite3.connect('rides.db')

cursor = conn.cursor()

#cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")

cursor.execute("DROP TABLE IF EXISTS RIDES")

cursor.execute("DROP TABLE IF EXISTS CONFIRMED_RIDES")

cursor.execute("DROP TABLE IF EXISTS RIDE_RATINGS")


#EMPLOYEE = '''CREATE TABLE EMPLOYEE(
#FNAME VARCHAR(50),
#LNAME VARCHAR(50),
#SID VARCHAR(10),
#INTERESTS VARCHAR(200))'''

#cursor.execute(EMPLOYEE)

RIDES='''CREATE TABLE RIDES(
RIDEID INT PRIMARY_KEY,
RIDERID VARCHAR(50),
RIDE_DATE VARCHAR(10),
RIDE_TIME VARCHAR(5),
RIDE_AVAIL VARCHAR(1)
)'''

cursor.execute(RIDES)

CONFIRMED_RIDES = '''CREATE TABLE CONFIRMED_RIDES(
RIDEID INT PRIMARY_KEY,
REQUESTOR VARCHAR(10),
OFFERER VARCHAR(10)
)'''

cursor.execute(CONFIRMED_RIDES)

RIDE_RATINGS = '''CREATE TABLE RIDE_RATINGS(
RIDEID INT PRIMARY_KEY,
REQUESTOR VARCHAR(10),
OFFERER VARCHAR(10),
OFFERER_RATING INT, 
OFFERER_EXP VARCHAR(200),
REQUESTOR_RATING INT, 
REQUESTOR_EXP VARCHAR(200)
)'''

cursor.execute(RIDE_RATINGS)

#INSERT INTO RIDES TABLE
insert_rides='''INSERT INTO RIDES VALUES (1,"B001","2023-06-16","07:30","Y"), (2,"B001","2023-06-17","08:30","Y")'''

cursor.execute(insert_rides)


#insert_emp = '''INSERT INTO EMPLOYEE
#VALUES ("BALU","BANDLAMUDI","B001","PAYMENTS,CODING,PYTHON,MOVIE"),
#       ("SIVA","KRISHNAN","S001","FOOTBALL,CODING,PYTHON,MOVIES,MUSIC")'''

#cursor.execute(insert_emp)


SELECT_EMP = '''SELECT * FROM EMPLOYEE'''

cursor.execute(SELECT_EMP)

rows=cursor.fetchall()
for row in rows:
    print(row)

SELECT_RIDES = ''' SELECT * FROM RIDES'''

cursor.execute(SELECT_RIDES)

rows=cursor.fetchall()

for row in rows:
    print(row)


conn.commit()

conn.close()

