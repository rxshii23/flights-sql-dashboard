import mysql.connector
# connect to database server
try:
    conn = mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        password='iRishi@23',
        auth_plugin='mysql_native_password',
        database='indigo'
    )
    mycursor = conn.cursor()
    print("connection successful")
except:
    print('connection error')

# create a database server

mycursor.execute("CREATE DATABASE flights")
conn.commit()

# create a table
# airport -> airport_id, code, name, city

# mycursor.execute("""
#     CREATE TABLE airport(
#         airport_id INTEGER PRIMARY KEY,
#         code VARCHAR(10) NOT NULL,
#         city VARCHAR(520) NOT NULL,
#         name VARCHAR(250) NOT NULL
#     )
#
# """)
# conn.commit()

# insert data to the table

# mycursor.execute("""
#     INSERT INTO  airport VALUES
#     (1, 'DEL', 'New Delhi', 'IGIA'),
#     (2, 'BOM', 'Mumbai', 'CSIT'),
#     (3, 'CCU', 'Kolkata', 'NSCA')
# """)
# conn.commit()

# search/retrieve
# mycursor.execute("SELECT * FROM airport WHERE airport_id > 1")
# data = mycursor.fetchall()
# print(data)
#
# for i in data:
#     print(i[3])

# update

# mycursor.execute("UPDATE airport SET city = 'Bombay' WHERE airport_id = 2")
# conn.commit()
# mycursor.execute("SELECT * FROM airport")
# data = mycursor.fetchall()
# print(data)


# delete

# mycursor.execute("DELETE FROM airport WHERE airport_id = 3")
# conn.commit()
# mycursor.execute("SELECT * FROM airport")
# data = mycursor.fetchall()
# print(data)
