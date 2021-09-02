# much of this code was adapted for demonstration
# purposes from freecodecamp.org

import mysql.connector
from mysql.connector import Error
import pandas as pd

#connects to MySQL Server using parameters as login credentials
def create_server_connection(host_name, user_name, user_password):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password
        )
        print("MySQL server connection successful")
    except Error as err:
        print(f"Error: '{err}'")
    return connection

#once we have connected to the server, this creates a database on it
def create_database(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Database created successfully")
    except Error as err:
        print(f"Error: '{err}'")

#once we have created a database, this connects directly to it
def create_db_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")
    return connection

#executes SQL data creation commands over the provided connection
def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query successful")
    except Error as err:
        print(f"Error: '{err}'")

#executes SQL query and returns the result as printable data
def read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as err:
        print(f"Error: '{err}'")

#get the MySQL password from user, then create our connection variable
pw = input("Please enter your MySQL Server password: ")
connection = create_server_connection("localhost", "root", pw)

#create a database called 'scores' over the provided server connection
create_database(connection, "CREATE DATABASE scores")

#connect directly to the 'scores' database
pw = input("Please enter your database password: ")
connection = create_db_connection("localhost", "root", pw, "scores")

#define and execute queries that populate 'scores' with two tables of data

createscores1 = """
CREATE TABLE ninecardpokerscores
(
    PlayerID int,
    FirstName varchar(100),
    LastName varchar(100),
    HighScore int,
    PRIMARY KEY(PlayerID)
);
"""

insertinscores1 = """
INSERT INTO ninecardpokerscores VALUES
(1, 'Daniel', 'Magnusson', 62),
(2, 'Mark', 'Kimble', 59),
(3, 'Cindy', 'Varna', 40),
(4, 'Tiffany', 'Peters', 68);  
"""

createscores2 = """
CREATE TABLE moreninecardpokerscores
(
    PlayerID int,
    FirstName varchar(100),
    LastName varchar(100),
    HighScore int,
    PRIMARY KEY(PlayerID)
);
"""

insertinscores2 = """
INSERT INTO moreninecardpokerscores VALUES
(5, 'Darren', 'Mulhoney', 33),
(6, 'Dino', 'Hendricksen', 71),
(7, 'Jennifer', 'Zimmerman', 68);  
"""

execute_query(connection, createscores1)
execute_query(connection, insertinscores1)
execute_query(connection, createscores2)
execute_query(connection, insertinscores2)

# define and execute a query that prints all and only the players whose
# first names start with D, in order of descending high score

selectdata = """
SELECT * FROM
(SELECT * FROM ninecardpokerscores 
UNION 
SELECT * FROM moreninecardpokerscores) AS totalscores
WHERE FirstName LIKE 'D%'
ORDER BY HighScore DESC;
"""

connection = create_db_connection("localhost", "root", pw, "scores")
results = read_query(connection, selectdata)
for entry in results:
    print(entry)

# finally, destroy our sample tables and sample database

execute_query(connection, "DROP TABLE ninecardpokerscores")
execute_query(connection, "DROP TABLE moreninecardpokerscores")
execute_query(connection, "DROP DATABASE scores")